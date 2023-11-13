from django import forms

class VendorForm(forms.Form):
    customer_id = forms.CharField(
        label='Vendor Id',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    company = forms.CharField(
        label='Company',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    phone = forms.CharField(
        label='HandPhone',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    tax = forms.CharField(
        label='Tax Information',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    website = forms.CharField(
        label='Website',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    linkedIn = forms.CharField(
        label='LinkedIn',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    facebook = forms.CharField(
        label='Facebook',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    tiktok = forms.CharField(
        label='TikTok',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    delivery_address = forms.CharField(
        label='Delivery Address',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )