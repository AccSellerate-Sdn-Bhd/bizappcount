from django import forms
from sales.models import Stakeholder


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields =         fields = [
            'customer_id', 'name','company',
            'email','handphone','address','delivery_address','tax_information','website',
            'linkedin', 'facebook',
            'tiktok','type'
        ]  # Use all fields from the model in the form.

