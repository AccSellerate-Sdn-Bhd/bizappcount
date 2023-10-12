from django import forms
from .models import Expense,Product,ExpenseLineItem

class ExpensesForm(forms.ModelForm):
    #customer_id = forms.ModelChoiceField(queryset=Customer.objects.all())


    class Meta:
        model = Expense
        fields = [
            'expense_id', 'title',
            'type',
            'payee', 'date', 'due_date',
            'status','recurring','recurring_amount', 'recurring_date'
        ]


class ExpensesLineItemsForm(forms.ModelForm):

    product_id = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = ExpenseLineItem
        fields = ['product_id', 'quantity', 'unit_discount', 'total_price']

class ExpensesLineItemswithIDForm(forms.ModelForm):

    product_id = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = ExpenseLineItem
        fields = ['expense_line_id','product_id', 'quantity', 'unit_discount', 'total_price']
