from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={'class': 'form-control w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': 'username'}),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': 'password'}),
    )

class AddressForm(forms.Form):
    line_one = forms.CharField(
        label='Line One',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_two = forms.CharField(
        label='Line Two',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    postcode = forms.CharField(
        label='Postcode',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    state = forms.CharField(
        label='State',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    gps_location = forms.CharField(
        label='GPS Location',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    office_tel_no = forms.CharField(
        label='Office Telephone Number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )

class Onboard1Form(UserCreationForm):
    class Meta:
        model = User  # Use your custom user model
        fields = ['username', 'category']

    CATEGORIES=[
        ('type1', "Type 1"),
        ('type2', "Type 2")
    ]

    username = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    category = forms.ChoiceField(
        choices=CATEGORIES,
        widget=forms.Select(attrs={'class': 'border p-2 h-12 w-full rounded mb-4 mt-2'})
    )
    password1 = forms.CharField(
        label='Password',
        initial="secret123",
        widget=forms.PasswordInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        initial="secret123",
        widget=forms.PasswordInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )


class Onboard2Form(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    type = forms.CharField(
        label='Business Type',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    registration_no = forms.CharField(
        label='Registration Number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    website_url = forms.CharField(
        label='Website Url',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_one = forms.CharField(
        label='Address Line One',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_two = forms.CharField(
        label='Address Line Two',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    postcode = forms.CharField(
        label='Postcode',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    state = forms.CharField(
        label='State',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    gps_location = forms.CharField(
        label='GPS Location',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    office_tel_no = forms.CharField(
        label='Office telephone number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )


class Onboard3Form(forms.Form):
    start_month = forms.ChoiceField(
        label='Tempoh Perakaunan Mula',
        choices=[('', 'Select a month')] + [(month, month)
                                            for month in range(1, 13)],
        widget=forms.Select(attrs={'class': 'border p-2 w-full rounded pl-8'}),
    )

    end_month = forms.ChoiceField(
        label='Tempoh Perakaunan Tamat',
        choices=[('', 'Select a month')] + [(month, month)
                                            for month in range(1, 13)],
        widget=forms.Select(attrs={'class': 'border p-2 w-full rounded pl-8'}),
    )

    agree_to_data_usage = forms.BooleanField(
        label='Saya setuju untuk menggunakan Data Jualan saya dari BizApp didalam sistem BizApp count',
        required=False,  # Makes the checkbox optional
        widget=forms.CheckboxInput(
            attrs={'class': 'w-5 h-5 rounded-full border border-gray-300 mr-2'}),
    )
