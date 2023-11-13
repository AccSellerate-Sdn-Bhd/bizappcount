from django.shortcuts import render
from .models import Expense,ExpenseLineItem,Product
from .forms import ExpensesForm,ExpensesLineItemsForm,ExpensesLineItemswithIDForm,ReceiptForm,DOForm
from inventory.models import Inventory, InventoryHistory
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.http import FileResponse

from report.models import TransactionAction, Journal
from user_onboard.models import User
import generatedoc
from django.shortcuts import redirect,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import ExpenseSerializer



@api_view(['POST'])
def create_expense_api(request):
    serializer = ExpenseSerializer(data=request.data)
    
    if serializer.is_valid():
        
        # Extract related data
        line_items_data = serializer.validated_data.pop('line_items', [])
        
        # Create Expense instance
        expense_instance = Expense.objects.create(**serializer.validated_data)
        
        # Create and link line items
        for item_data in line_items_data:
            ExpenseLineItem.objects.create(expense_id=expense_instance, **item_data)
            
        return Response({"success": True}, status=status.HTTP_201_CREATED)
    else:
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



#SalesLineItemsFormSet = modelformset_factory(SalesLineItems, form=SalesLineItemsForm, extra=1)
@login_required
def expenses_dashboard(request):

    expenses = Expense.objects.annotate(total_amount=Sum('line_items__total_price'))
    expenses_line_data = ExpenseLineItem.objects.all()

    context = {
        'url': "/dashboard/expenses",
        'expenses_data': expenses,
        'expenses_line_data': expenses_line_data,
    }
    print(context)
    return render(request, 'expenses/expenses_dashboard.html', context)

@login_required
def create_expenses(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')    
    # Define the formset class
    ExpenseLineItemsFormSet = modelformset_factory(ExpenseLineItem, form=ExpensesLineItemsForm, extra=1)
    all_products = serialize('json', Product.objects.all())
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        formset = ExpenseLineItemsFormSet(request.POST, prefix="lineitems")
        #shipform = ShippingForm(request.POST)
        print(form.errors)
        print(formset.errors)
        if form.is_valid() and formset.is_valid():
            expense_instance = form.save(commit=False)
            print(form.cleaned_data)
            expense_instance.user_id = request.user
            expense_instance.save()

            # Save each form in the formset
            for item_form in formset:
                item_instance = item_form.save(commit=False)
                item_instance.expense_id = expense_instance
                item_instance.save()

            runTransactionAction(expense_instance, user)
            # You should redirect after successful POST (PRG pattern)
            return redirect("/dashboard/expenses/")
        else:
            messages.error(request, 'Failed to create expenses entry. Please correct the errors below.')
    else:
        form = ExpensesForm()
        formset = ExpenseLineItemsFormSet(queryset=ExpenseLineItem.objects.none(), prefix="lineitems")

    return_value = {
        'url': "/dashboard/expenses",
        'form': form,
        "formset": formset,
        'all_products':all_products
    }

    return render(request, 'expenses/create_expense.html', return_value)


@login_required
def delete_expenses(request, expense_id):
    try:
        expense = Expense.objects.get(pk=expense_id)
        
        # Delete related SalesLine items
        ExpenseLineItem.objects.filter(expense_id=expense_id).delete()
        
        
        # Finally, delete the Sales record
        expense.delete()

        # Optionally, add a message using Django's messages framework to inform user of successful delete.

    except Expense.DoesNotExist:
        # Handle the error, e.g. show a 404 error page, or redirect back with an error message.
        pass
    
    return redirect('expenses_dashboard')

@login_required
def delete_expenses_line(request, expenses_line_id):
    try:
        ExpenseLineItem.objects.get(pk=expenses_line_id).delete()
    

    except Expense.DoesNotExist:
        # Handle the error, e.g. show a 404 error page, or redirect back with an error message.
        pass
    
    return redirect('expenses_dashboard')

@login_required
def edit_expenses(request, expenses_id):
    # Fetch the existing sales instance
    existing_expense = get_object_or_404(Expense, expense_id=expenses_id)

    # Define the formset class
    ExpenseLineItemsFormSet = modelformset_factory(ExpenseLineItem, form=ExpensesLineItemsForm,extra=0)
    all_products = serialize('json', Product.objects.all())

    if request.method == 'POST':
        form = ExpensesForm(request.POST, instance=existing_expense)
        formset = ExpenseLineItemsFormSet(request.POST, prefix="lineitems", queryset=ExpenseLineItem.objects.filter(expense_id=existing_expense))

        print(form.is_valid())
        print(formset)


        if form.is_valid() and formset.is_valid() :
            expenses_instance = form.save()
            #print(request.POST)
            # Update line items
            for item_form in formset:
                item_instance = item_form.save(commit=False)
                item_instance.expense_id = expenses_instance
                item_instance.product_id = item_form.cleaned_data.get('product_id')
                print(item_instance)
                item_instance.save()


            return redirect("/dashboard/expenses")
        else:
            messages.error(request, 'Failed to update expenses entry. Please correct the errors below.')

    else:
        form = ExpensesForm(instance=existing_expense)
        formset = ExpenseLineItemsFormSet(prefix="lineitems", queryset=ExpenseLineItem.objects.filter(expense_id=existing_expense))

    return_value = {
        'url': "/dashboard/expenses",
        'form': form,
        "formset": formset,
        'all_products': all_products
    }

    return render(request, 'expenses/edit_template.html', return_value)


def generate_purchase_order(request, expenses_id):
    # Fetch the expense data
    expense = Expense.objects.get(expense_id=expenses_id)  # Assuming the primary key is id for the Expense model
    expense_lines = ExpenseLineItem.objects.filter(expense_id=expenses_id)

    # Use a PDF generation library to generate the PDF
    pdf = generatedoc.generate_professional_purchase_order(expense, expense_lines) # This function should return the binary data for the PDF

    # Return the PDF as a response
    response = FileResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="purchase_order_{expenses_id}.pdf"'

    return response



def upload_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receipt uploaded successfully!')
            return redirect('expenses_dashboard')  # This will redirect back to the dashboard after uploading.
        else:
            messages.error(request, 'There was a problem uploading the receipt.')
    else:
        form = ReceiptForm()

    return redirect('expenses_dashboard')  # If not POST, or if there's an error, just redirect back.


def upload_do(request):
    if request.method == "POST":
        form = DOForm(request.POST, request.FILES)
        print(form)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'DO uploaded successfully!')
            return redirect('expenses_dashboard')  # This will redirect back to the dashboard after uploading.
        else:
            messages.error(request, 'There was a problem uploading the delivery order.')
    else:
        form = DOForm()

    return redirect('expenses_dashboard')  # If not POST, or if there's an error, just redirect back.


def runTransactionAction(expense, user):
    print("\n\n\n")
    print(expense.title)
    title = expense.title
    datetime = expense.date
    actions = TransactionAction.objects.filter(expense_title=title, payment=expense.payment_type)
    print(actions)

    if(len(actions) >0):
        for action in actions:
            # Do something with item
            #print(action.name)
            #print(action.account.name)
            # relationship = AccountUserRelationship.objects.filter(account=action.account, user=user)

            if(action.model == "ExpenseLineItem"):
                modelExpenseLineItem(expense, datetime, action.datafield, action.operation, user, action.account)
            elif(action.model == "Product"):
                modelProduct(expense, datetime, action.datafield, action.operation, user, action.account)
            elif(action.model == "Inventory"):
                modelInventory(expense, action.operation, user)                


def modelExpenseLineItem(expenses, date, field, operation, user, account):
    expenseLineItems = ExpenseLineItem.objects.filter(expense_id=expenses)
    amount = 0

    for expenseLineItem in expenseLineItems:
        amount += float(getattr(expenseLineItem, field))

    new_journal = Journal(
        account = account,
        user = user,
        datetime =  date,
        name = account.name,
        debit_amount=amount if operation == 1 else None,
        credit_amount= None if operation == 1 else amount,
        description=expenses.title,
        editable=1
    )

    new_journal.save()

def modelProduct(expenses, date, field, operation, user, account):
    expenseLineItems = ExpenseLineItem.objects.filter(expense_id=expenses)
    amount = 0

    for expenseLineItem in expenseLineItems:
        amount += float(getattr(expenseLineItem.product_id, field)) * float(expenseLineItem.quantity)

    new_journal = Journal(
        account = account,
        user = user,
        datetime =  date,
        name = account.name,
        debit_amount=amount if operation == 1 else None,
        credit_amount= None if operation == 1 else amount,
        description=expenses.title,
        editable=1
    )

    new_journal.save()


def modelInventory(expense,  operation, user):

        expensesLineItems = ExpenseLineItem.objects.filter(expense_id=expense)

        for expensesLineItem in expensesLineItems:
            inventory = Inventory.objects.get(pk=expensesLineItem.product_id.product_id, user=user.user_id)

            editedFieldsString = "Expenses created, " + ("increase" if(operation) else "decrease")

            if (operation):
                increase = True
                amount = expensesLineItem.quantity
                current_stock = inventory.amount + expensesLineItem.quantity
            else:
                increase = False
                amount = abs(expensesLineItem.quantity)
                current_stock = inventory.amount - expensesLineItem.quantity

            inventory.amount = current_stock

            print("\n a lot of heart")
            print(expensesLineItem.product_id.product_id)
            print(amount)
            print(inventory)
            print(editedFieldsString)
            print("\n")

            new_inventory_history = InventoryHistory(
                inventory=inventory,
                description=editedFieldsString,
                increase=increase,
                amount=amount,
                current_stock=current_stock
            )

            inventory.save()
            new_inventory_history.save()

    