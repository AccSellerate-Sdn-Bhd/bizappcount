from django import forms
from .models import Sales, Stakeholder,Product,SalesLineItems ,ShippingInformation

class SalesForm(forms.ModelForm):
    customer_id = forms.ModelChoiceField(queryset=Stakeholder.objects.all())


    class Meta:
        model = Sales
        fields = [
            'sales_id', 'customer_id','title',
            'date',
            'closing_date', 'status',
            'recurring', 'recurring_date','payment_type'
        ]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = [
            'customer_id', 'name','company',
            'email','handphone','address','delivery_address','tax_information','website',
            'linkedin', 'facebook',
            'tiktok'
        ]  # Use all fields from the model in the form.


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