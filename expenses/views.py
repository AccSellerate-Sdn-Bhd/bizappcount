from django.shortcuts import render
from .models import Expense,ExpenseLineItem,Product
from .forms import ExpensesForm,ExpensesLineItemsForm,ExpensesLineItemswithIDForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.http import FileResponse
import generatedoc
from django.shortcuts import redirect,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser




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


            # You should redirect after successful POST (PRG pattern)
            return redirect("/expenses")
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
    ExpenseLineItemsFormSet = modelformset_factory(ExpenseLineItem, form=ExpensesLineItemswithIDForm,extra=0)
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


            return redirect("/expenses")
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