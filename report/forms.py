from django import forms
from datetime import datetime

class FilterForm(forms.Form):
    start_date = forms.DateField(
        label='Start Date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    
    end_date = forms.DateField(
        label='End Date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )