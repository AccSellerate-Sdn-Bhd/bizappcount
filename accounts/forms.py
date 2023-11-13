from django import forms

class AccountForm(forms.Form):
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
    account = forms.ChoiceField(
      label="Parent Account",
      required=False,
      widget=forms.Select(attrs={'class': 'border p-2 h-12 w-full rounded mb-4 mt-2'})
    )

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', None)
        super(AccountForm, self).__init__(*args, **kwargs)

        if dynamic_choices:
            self.fields['account'].choices = dynamic_choices