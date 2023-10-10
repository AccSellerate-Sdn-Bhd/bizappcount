from django import forms
from .models import Sales, Customer,Product,SalesLineItems ,ShippingInformation

class SalesForm(forms.ModelForm):
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.all())


    class Meta:
        model = Sales
        fields = [
            'sales_id', 'customer_id','title',
            'date',
            'document_number', 'closing_date', 'status',
            'recurring', 'recurring_date'
        ]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # Use all fields from the model in the form.


class SalesLineItemsForm(forms.ModelForm):

    product_id = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = SalesLineItems
        fields = ['product_id', 'quantity', 'unit_discount', 'total_price']


class SalesLineItemswithIDForm(forms.ModelForm):

    product_id = forms.ModelChoiceField(queryset=Product.objects.all())

    class Meta:
        model = SalesLineItems
        fields = ['sales_line_id','product_id', 'quantity', 'unit_discount', 'total_price']



class ShippingForm(forms.ModelForm):

    class Meta:
        model = ShippingInformation
        fields = ['shipping_no', 'tracking_no', 'weight', 'pricing']