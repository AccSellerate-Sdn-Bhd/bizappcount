from django import forms

class InventoryForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    amount = forms.CharField(
        label='Amount',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    unit = forms.CharField(
        label='Unit',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    price_per_unit = forms.CharField(
        label='Price per unit',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    product = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'border p-2 h-12 w-full rounded mb-4 mt-2'})
    )

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', None)
        super(InventoryForm, self).__init__(*args, **kwargs)

        if dynamic_choices:
            self.fields['product'].choices = dynamic_choices