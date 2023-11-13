from django import forms


class BillForm(forms.Form):
    RECURRING_INTERVAL_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ]

    name = forms.CharField(
        label='Bill Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    amount = forms.CharField(
        label='Bill Amount',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    recurring_interval = forms.ChoiceField(
        choices=RECURRING_INTERVAL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Recurring Interval'
    )