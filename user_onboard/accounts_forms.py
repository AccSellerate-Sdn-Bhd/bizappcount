from django import forms

class BankForm(forms.Form):
    name = forms.CharField(
        label='Bank Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    account_no = forms.CharField(
        label='Account number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    type = forms.CharField(
        label='Type',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    bizapp = forms.BooleanField(
        label='BizApp',  
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},
        ),
    )
    line_one = forms.CharField(
        label='Line One',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_two = forms.CharField(
        label='Line Two',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    postcode = forms.CharField(
        label='Postcode',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    city = forms.CharField(
        label='City',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    state = forms.CharField(
        label='State',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    gps_location = forms.CharField(
        label='GPS Location',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    office_tel_no = forms.CharField(
        label='Office Telephone Number',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    address = forms.ChoiceField(
        required=0,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
    )
    create_new_address = forms.BooleanField(
        label='Create new address?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': '', 'id': 'create_new_address', 'type': 'checkbox'},  
        ),
    )

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', None)
        super(BankForm, self).__init__(*args, **kwargs)

        if dynamic_choices:
            self.fields['address'].choices = dynamic_choices

class OfficeForm(forms.Form):
    name = forms.CharField(
        label='Office Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    rent = forms.BooleanField(
        label='Rent', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},  
        ),
    )
    electric = forms.CharField(
        label='Electric',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    water = forms.CharField(
        label='Water',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    internet = forms.CharField(
        label='Internet',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    rental = forms.CharField(
        label='Rental',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    rental_deposit = forms.CharField(
        label='Rental Deposit',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_one = forms.CharField(
        label='Line One',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_two = forms.CharField(
        label='Line Two',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    postcode = forms.CharField(
        label='Postcode',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    city = forms.CharField(
        label='City',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    state = forms.CharField(
        label='State',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    gps_location = forms.CharField(
        label='GPS Location',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    office_tel_no = forms.CharField(
        label='Office Telephone Number',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    address = forms.ChoiceField(
        required=0,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
    )
    create_new_address = forms.BooleanField(
        label='Create new address?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': '', 'id': 'create_new_address', 'type': 'checkbox'},  
        ),
    )

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', None)
        super(OfficeForm, self).__init__(*args, **kwargs)

        if dynamic_choices:
            self.fields['address'].choices = dynamic_choices

class StaffForm(forms.Form):
    name = forms.CharField(
        label='Staff Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    ic_passport = forms.CharField(
        label='IC/Passport Number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    type = forms.CharField(
        label='Type',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    phone_no = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    date_joined = forms.DateField(
        label='Date Joined',
        widget=forms.DateInput(
            attrs={'class': 'datepicker w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': 'Select a date'}),
        input_formats=['%Y-%m-%d'],
    )
    position = forms.CharField(
        label='Position',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    salary = forms.CharField(
        label='Salary',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    epf = forms.CharField(
        label='EPF',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )

    line_one = forms.CharField(
        label='Line One',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_two = forms.CharField(
        label='Line Two',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    postcode = forms.CharField(
        label='Postcode',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    city = forms.CharField(
        label='City',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    state = forms.CharField(
        label='State',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    gps_location = forms.CharField(
        label='GPS Location',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    office_tel_no = forms.CharField(
        label='Office Telephone Number',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    address = forms.ChoiceField(
        required=0,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
    )
    create_new_address = forms.BooleanField(
        label='Create new address?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': '', 'id': 'create_new_address', 'type': 'checkbox'},  
        ),
    )

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', None)
        super(StaffForm, self).__init__(*args, **kwargs)

        if dynamic_choices:
            self.fields['address'].choices = dynamic_choices

class ProductForm(forms.Form):
    name = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    description = forms.CharField(
        label='Product Description',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    brand = forms.CharField(
        label='Brand',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    collection = forms.CharField(
        label='Collection',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    SKU = forms.CharField(
        label='SKU',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    barcode = forms.CharField(
        label='Barcode',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    weight = forms.CharField(
        label='Weight',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    height = forms.CharField(
        label='Height',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    width = forms.CharField(
        label='Width',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    length = forms.CharField(
        label='Length',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    cost = forms.CharField(
        label='Cost',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    forex = forms.CharField(
        label='Forex',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    retail_selling_price = forms.CharField(
        label='Retail Selling Price',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    status = forms.CharField(
        label='Status',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )

class LoanForm(forms.Form):
    name = forms.CharField(
        label='Loan Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    category = forms.CharField(
        label='Category',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    creditor = forms.CharField(
        label='Creditor name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    creditor_phone_no = forms.CharField(
        label="Creditor's Phone Number",
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    amount = forms.CharField(
        label='Amount',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    amount_payable = forms.CharField(
        label='Amount Payable',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    interest = forms.CharField(
        label='Interest',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    installment_amount = forms.CharField(
        label='Installment Amount',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    not_defined = forms.BooleanField(
        label='Not defined?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},  
        ),
    )
    recurring = forms.BooleanField(
        label='Recurring?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},  
        ),
    )
    active = forms.BooleanField(
        label='Active?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},  
        ),
    )
    line_one = forms.CharField(
        label='Line One',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    line_two = forms.CharField(
        label='Line Two',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    postcode = forms.CharField(
        label='Postcode',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    city = forms.CharField(
        label='City',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    state = forms.CharField(
        label='State',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    gps_location = forms.CharField(
        label='GPS Location',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    office_tel_no = forms.CharField(
        label='Office Telephone Number',
        required=0,
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    address = forms.ChoiceField(
        required=0,
        widget=forms.RadioSelect(attrs={'class': 'radio'}),
    )
    create_new_address = forms.BooleanField(
        label='Create new address?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': '', 'id': 'create_new_address', 'type': 'checkbox'},  
        ),
    )

    def __init__(self, *args, **kwargs):
        dynamic_choices = kwargs.pop('dynamic_choices', None)
        super(LoanForm, self).__init__(*args, **kwargs)

        if dynamic_choices:
            self.fields['address'].choices = dynamic_choices

class SoftwareCostForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    type = forms.CharField(
        label='Type',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    software_billing_info = forms.CharField(
        label='Software Billing Info',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    company_name = forms.CharField(
        label='Company Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    billing_duration = forms.CharField(
        label='Billing Duration',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    amount = forms.CharField(
        label='Amount',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    active = forms.BooleanField(
        label='Active?', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},  
        ),
    )

class OwnerEquityForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    ic_passport = forms.CharField(
        label='IC/Passport Number',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    nationality = forms.CharField(
        label='Nationality',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    bumiputera = forms.BooleanField(
        label='Check if Bumiputera', 
        required=0,
        widget=forms.CheckboxInput(
            attrs={'class': ''},  
        ),
    )
    percentage_ownership = forms.CharField(
        label='Percentage Ownership',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )
    paid_up_capital = forms.CharField(
        label='Paid Up Capital',
        widget=forms.TextInput(
            attrs={'class': 'w-full p-2 border border-gray-300 rounded mb-4 mt-2', 'placeholder': ''}),
    )