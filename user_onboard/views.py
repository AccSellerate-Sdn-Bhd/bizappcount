from django.shortcuts import render, redirect
from .forms import LoginForm, Onboard1Form, Onboard2Form
from .accounts_forms import BankForm, OfficeForm, StaffForm, ProductForm, LoanForm, SoftwareCostForm, OwnerEquityForm
from .models import User, Address, Business, Bank, Office, Staff, Product, Loan, SoftwareCost, OwnerEquity
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.


def login(request):
    if (request.user != "AnonymousUser"):
        logout(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                print("im here")
                # 'selected_option' now contains the value of the selected radio button
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    print("done login")

                    return redirect('/dashboard')
                else:
                    print("Login failed")
                    form.add_error(None, "User does not exist")
                return render(request, 'pages/login.html', {'form': form})
            except Exception as e:
                error_message = str(e)
                print(error_message)
                form.add_error(None, error_message)
                return render(request, 'pages/login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})


def onboard_1(request):
    if request.method == 'POST':
        form = Onboard1Form(request.POST)

        if form.is_valid():
            print("Form is valid")
            new_user = form.save()

            user = authenticate(request, username=new_user.username,
                                password=form.cleaned_data['password2'])
            if user is not None:
                auth_login(request, user)
                print("Save" + str(new_user.pk) + str(new_user))

                return redirect('/register/user/2')
            else:
                print("Login failed")
                return

    else:
        form = Onboard1Form()

    return render(request, 'pages/onboard_1.html', {'form': form})


def onboard_2(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/login')

    if request.method == 'POST':
        form = Onboard2Form(request.POST)
        if form.is_valid():
            try:
                new_address = Address(
                    line_one=form.cleaned_data['line_one'],
                    line_two=form.cleaned_data['line_two'],
                    postcode=form.cleaned_data['postcode'],
                    city=form.cleaned_data['city'],
                    state=form.cleaned_data['state'],
                    GPS_location=form.cleaned_data['gps_location'],
                    office_tel_no=form.cleaned_data['office_tel_no'],
                    user=user
                )

                new_address.save()

                new_business = Business(
                    name=form.cleaned_data['name'],
                    type=form.cleaned_data['type'],
                    address=new_address,
                    registration_no=form.cleaned_data['registration_no'],
                    website_url=form.cleaned_data['website_url'],
                    user=user
                )

                new_business.save()

                return redirect('/register/user/3')
            except Exception as e:
                error_message = str(e)

                if (error_message.find('registration_no') != -1):
                    error_message = "Please enter number of 'Registration Number'"
                elif (error_message.find('postcode') != -1):
                    error_message = "Please enter number of 'Postcode'"
                else:
                    error_message = "Error encountered, please check if all fields are filled"

                form.add_error(None, error_message)

                return render(request, 'pages/onboard_2.html', {'form': form})

        else:
            return render(request, 'pages/onboard_2.html', {'form': form})
    else:
        form = Onboard2Form()

    return render(request, 'pages/onboard_2.html', {'form': form, 'name': user.username})


def onboard_3(request):
    try:
        user = User.objects.get(username=request.user)
        business = Business.objects.get(user=user)
        address = Address.objects.get(user=user)
    except Exception as e:
        return redirect('/')

    return render(request, 'pages/onboard_3.html', {'name': user.username, 'business': business, 'address': address})


def onboard_4(request):
    try:
        user = User.objects.get(username=request.user)
        business = Business.objects.get(user=user)
        banks = Bank.objects.filter(user=user)
        offices = Office.objects.filter(user=user)
        staffs = Staff.objects.filter(user=user)
        products = Product.objects.filter(user=user)
        loans = Loan.objects.filter(user=user)
        software_costs = SoftwareCost.objects.filter(user=user)
        owner_equities = OwnerEquity.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    print("\n")
    print(offices)

    return render(request, 'pages/onboard_4.html', {
        'user': user,
        'requeat': request,
        'business': business,
        'banks': banks,
        'offices': offices,
        'staffs': staffs,
        'products': products,
        'loans': loans,
        'software_costs': software_costs,
        'owner_equities': owner_equities
    })


def create_bank(request):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    choices_list = [(address.address_id, address) for address in addresses]

    form = BankForm(dynamic_choices=choices_list)

    if request.method == 'POST':
        form = BankForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():
            print(form.cleaned_data['create_new_address'])

            try:
                if(form.cleaned_data['create_new_address']):
                    new_address = Address(
                        line_one=form.cleaned_data['line_one'],
                        line_two=form.cleaned_data['line_two'],
                        postcode=form.cleaned_data['postcode'],
                        city=form.cleaned_data['city'],
                        state=form.cleaned_data['state'],
                        GPS_location=form.cleaned_data['gps_location'],
                        office_tel_no=form.cleaned_data['office_tel_no'],
                        user=user
                    )

                    new_address.save()

                    new_bank = Bank(
                        user=user,
                        name=form.cleaned_data['name'],
                        account_no=form.cleaned_data['account_no'],
                        address=new_address,
                        type=form.cleaned_data['type'],
                        bizapp=form.cleaned_data['bizapp'],
                    )

                    new_bank.save()

                    return redirect("/dashboard/account-setup")
                else:
                    print(form.cleaned_data['address'])
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])

                    new_bank = Bank(
                        user=user,
                        name=form.cleaned_data['name'],
                        account_no=form.cleaned_data['account_no'],
                        address=existing_address,
                        type=form.cleaned_data['type'],
                        bizapp=form.cleaned_data['bizapp'],
                    )

                    new_bank.save()

                    return redirect("/dashboard/account-setup")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/bank_page.html', {'form': form})


        else:
            return render(request, 'pages/formPages/bank_page.html', {'form': form})
    else:
        return render(request, 'pages/formPages/bank_page.html', {'form': form})



def create_office(request):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    choices_list = [(address.address_id, address) for address in addresses]

    form = OfficeForm(dynamic_choices=choices_list)

    if request.method == 'POST':
        form = OfficeForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():
            try:
                if(form.cleaned_data['create_new_address']):
                    new_address = Address(
                        line_one=form.cleaned_data['line_one'],
                        line_two=form.cleaned_data['line_two'],
                        postcode=form.cleaned_data['postcode'],
                        city=form.cleaned_data['city'],
                        state=form.cleaned_data['state'],
                        GPS_location=form.cleaned_data['gps_location'],
                        office_tel_no=form.cleaned_data['office_tel_no'],
                        user=user
                    )

                    new_address.save()

                    new_office = Office(
                        user=user,
                        name=form.cleaned_data['name'],
                        address=new_address,

                        rent=form.cleaned_data['rent'],
                        electric=int(
                            form.cleaned_data['electric']) if form.cleaned_data['electric'] else 0,
                        water=int(form.cleaned_data['water']
                                ) if form.cleaned_data['water'] else 0,
                        internet=int(
                            form.cleaned_data['internet']) if form.cleaned_data['internet'] else 0,
                        rental=int(form.cleaned_data['rental']
                                ) if form.cleaned_data['rental'] else 0,
                        rental_deposit=int(
                            form.cleaned_data['rental_deposit']) if form.cleaned_data['rental_deposit'] else 0,
                    )

                    new_office.save()

                    return redirect("/dashboard/account-setup")
                else:
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])
                    new_office = Office(
                        user=user,
                        name=form.cleaned_data['name'],
                        address=existing_address,

                        rent=form.cleaned_data['rent'],
                        electric=int(
                            form.cleaned_data['electric']) if form.cleaned_data['electric'] else 0,
                        water=int(form.cleaned_data['water']
                                ) if form.cleaned_data['water'] else 0,
                        internet=int(
                            form.cleaned_data['internet']) if form.cleaned_data['internet'] else 0,
                        rental=int(form.cleaned_data['rental']
                                ) if form.cleaned_data['rental'] else 0,
                        rental_deposit=int(
                            form.cleaned_data['rental_deposit']) if form.cleaned_data['rental_deposit'] else 0,
                    )

                    new_office.save()

                    return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/office_page.html', {'form': form})
        else:
            form = OfficeForm(request, dynamic_choices=choices_list)
 
    return render(request, 'pages/formPages/office_page.html', {'form': form})


def create_staff(request):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    choices_list = [(address.address_id, address) for address in addresses]

    form = StaffForm(dynamic_choices=choices_list)

    if request.method == 'POST':
        form = StaffForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():
            try:
                if(form.cleaned_data['create_new_address']):
                    new_address = Address(
                        line_one=form.cleaned_data['line_one'],
                        line_two=form.cleaned_data['line_two'],
                        postcode=form.cleaned_data['postcode'],
                        city=form.cleaned_data['city'],
                        state=form.cleaned_data['state'],
                        GPS_location=form.cleaned_data['gps_location'],
                        office_tel_no=form.cleaned_data['office_tel_no'],
                        user=user
                    )

                    new_address.save()

                    new_staff = Staff(
                        user=user,
                        name=form.cleaned_data['name'],
                        address=new_address,

                        ic_passport = form.cleaned_data['ic_passport'],
                        type = form.cleaned_data['type'],
                        phone_no = form.cleaned_data['phone_no'],
                        date_joined = form.cleaned_data['date_joined'],
                        position = form.cleaned_data['position'],
                        salary = float(form.cleaned_data['salary']),
                        epf = float(form.cleaned_data['epf']),
                    )

                    new_staff.save()

                    return redirect("/dashboard/account-setup")
                else:
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])
                    
                    new_staff = Staff(
                        user=user,
                        name=form.cleaned_data['name'],
                        address=existing_address,

                        ic_passport = form.cleaned_data['ic_passport'],
                        type = form.cleaned_data['type'],
                        phone_no = form.cleaned_data['phone_no'],
                        date_joined = form.cleaned_data['date_joined'],
                        position = form.cleaned_data['position'],
                        salary = float(form.cleaned_data['salary']),
                        epf = float(form.cleaned_data['epf']),
                    )

                    new_staff.save()

                    return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/staff_page.html', {'form': form})
        else:
            form = StaffForm(request, dynamic_choices=choices_list)
 
    return render(request, 'pages/formPages/staff_page.html', {'form': form})


def create_product(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')
    
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            try:
                new_product = Product(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    brand = form.cleaned_data['brand'],
                    collection = form.cleaned_data['collection'],
                    SKU = form.cleaned_data['SKU'],
                    barcode = form.cleaned_data['barcode'],
                    weight = int(form.cleaned_data['weight']) if form.cleaned_data['weight'] else None,
                    height = int(form.cleaned_data['height']) if form.cleaned_data['height'] else None,
                    width = int(form.cleaned_data['width']) if form.cleaned_data['width'] else None,
                    length = int(form.cleaned_data['length']) if form.cleaned_data['length'] else None,
                    cost = form.cleaned_data['cost'],
                    forex = form.cleaned_data['forex'],
                    retail_selling_price = form.cleaned_data['retail_selling_price'],
                    status = form.cleaned_data['status'],
                    user=user
                )

                new_product.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/product_page.html', {'form': form})
        else:
            print(form.errors)
            form = ProductForm(request.POST)
 
    return render(request, 'pages/formPages/product_page.html', {'form': form})


def create_loan(request):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    choices_list = [(address.address_id, address) for address in addresses]

    form = LoanForm(dynamic_choices=choices_list)

    if request.method == 'POST':
        form = LoanForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():
            try:
                if(form.cleaned_data['create_new_address']):
                    new_address = Address(
                        line_one=form.cleaned_data['line_one'],
                        line_two=form.cleaned_data['line_two'],
                        postcode=form.cleaned_data['postcode'],
                        city=form.cleaned_data['city'],
                        state=form.cleaned_data['state'],
                        GPS_location=form.cleaned_data['gps_location'],
                        office_tel_no=form.cleaned_data['office_tel_no'],
                        user=user
                    )

                    new_address.save()

                    new_loan = Loan(
                        user=user,
                        name = form.cleaned_data['name'],
                        category = form.cleaned_data['category'],
                        creditor = form.cleaned_data['creditor'],
                        creditor_address = new_address,
                        creditor_phone_no = form.cleaned_data['creditor_phone_no'],
                        
                        amount = form.cleaned_data['amount'],
                        amount_payable = form.cleaned_data['amount_payable'],
                        interest = form.cleaned_data['interest'],
                        installment_amount = form.cleaned_data['installment_amount'],
                        not_defined = form.cleaned_data['not_defined'],
                        recurring = form.cleaned_data['recurring'],
                        active = form.cleaned_data['active'],
                        )

                    new_loan.save()

                    return redirect("/dashboard/account-setup")
                else:
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])
                    
                    new_loan = Loan(
                        user=user,
                        name = form.cleaned_data['name'],
                        category = form.cleaned_data['category'],
                        creditor = form.cleaned_data['creditor'],
                        creditor_address = existing_address,
                        creditor_phone_no = form.cleaned_data['creditor_phone_no'],
                        
                        amount = form.cleaned_data['amount'],
                        amount_payable = form.cleaned_data['amount_payable'],
                        interest = form.cleaned_data['interest'],
                        installment_amount = form.cleaned_data['installment_amount'],
                        not_defined = form.cleaned_data['not_defined'],
                        recurring = form.cleaned_data['recurring'],
                        active = form.cleaned_data['active'],
                        )

                    new_loan.save()

                    return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/loan_page.html', {'form': form})
        else:
            form = LoanForm(request, dynamic_choices=choices_list)
 
    return render(request, 'pages/formPages/loan_page.html', {'form': form})

def create_software_cost(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')
    
    form = SoftwareCostForm()

    if request.method == 'POST':
        form = SoftwareCostForm(request.POST)

        if form.is_valid():
            try:
                new_software_cost = SoftwareCost(
                    name = form.cleaned_data['name'],
                    type = form.cleaned_data['type'],
                    software_billing_info = form.cleaned_data['software_billing_info'],
                    company_name = form.cleaned_data['company_name'],
                    billing_duration = form.cleaned_data['billing_duration'],
                    amount = form.cleaned_data['amount'],
                    active = form.cleaned_data['active'],
                    user=user
                )

                new_software_cost.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/software_page.html', {'form': form})
        else:
            print(form.errors)
            form = SoftwareCostForm(request.POST)
 
    return render(request, 'pages/formPages/software_page.html', {'form': form})


def create_owner_equity(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')
    
    form = OwnerEquityForm()

    if request.method == 'POST':
        form = OwnerEquityForm(request.POST)

        if form.is_valid():
            try:
                new_owner_equity = OwnerEquity(
                    name = form.cleaned_data['name'],
                    ic_passport = form.cleaned_data['ic_passport'],
                    nationality = form.cleaned_data['nationality'],
                    bumiputera = form.cleaned_data['bumiputera'],
                    percentage_ownership = form.cleaned_data['percentage_ownership'],
                    paid_up_capital = form.cleaned_data['paid_up_capital'],
                    user=user
                )

                new_owner_equity.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/equity_page.html', {'form': form})
        else:
            print(form.errors)
            form = OwnerEquityForm(request.POST)
 
    return render(request, 'pages/formPages/equity_page.html', {'form': form})

