from django.shortcuts import render, redirect
from .forms import LoginForm, Onboard1Form, Onboard2Form
from .accounts_forms import BankForm, OfficeForm, StaffForm, ProductForm, LoanForm, SoftwareCostForm, OwnerEquityForm
from .models import User, Address, Business, Bank, Office, Staff, Product, Loan, SoftwareCost, OwnerEquity
from django.contrib.auth import authenticate, login as auth_login, logout
from report.models import AccountUserRelationship, Account
from .functions.bank.views import bank_create, bank_edit
from .functions.office.views import office_create, office_edit
from .functions.staff.views import staff_create, staff_edit
from .functions.product.views import product_create, product_edit
from .functions.loan.views import loan_create, loan_edit
from .functions.software.views import software_cost_create, software_cost_edit
from .functions.equity.views import owner_equity_create, owner_equity_edit
from django.http import JsonResponse
from datetime import datetime as DateFunction

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
            createUserAccounts(new_user)

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

def createUserAccounts(user):

    def createAccount(account):
        newuseraccount = AccountUserRelationship(
            user=user,
            account=account,
            amount= 0
        )
        newuseraccount.save()

    cash_account = Account.objects.get(name="Cash Account")
    account_receivables = Account.objects.get(name="Account Receivables")
    inventory = Account.objects.get(name="Inventory")
    raw_materials = Account.objects.get(name="Raw Materials")

    machine_and_equipment = Account.objects.get(name="Machine and Equipment")
    investments = Account.objects.get(name="Investments")
    accumulated_depreciation = Account.objects.get(name="Accumulated Depreciation")

    account_payable = Account.objects.get(name="Account Payable")
    short_term_debt = Account.objects.get(name="Short Term Debt")
    long_term_debt = Account.objects.get(name="Long Term Debt")

    owners_capital = Account.objects.get(name="Owners Capital")
    retained_earnings = Account.objects.get(name="Retained Earnings")

    createAccount(cash_account)
    createAccount(account_receivables)
    createAccount(inventory)
    createAccount(raw_materials)

    createAccount(machine_and_equipment)
    createAccount(investments)
    createAccount(accumulated_depreciation)

    createAccount(account_payable)
    createAccount(short_term_debt)
    createAccount(long_term_debt)
    
    createAccount(owners_capital)
    createAccount(retained_earnings)


    


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
        banks = Bank.objects.filter(user=user, deleted=False)
        offices = Office.objects.filter(user=user, deleted=False)
        staffs = Staff.objects.filter(user=user, deleted=False)
        products = Product.objects.filter(user=user, deleted=False)
        loans = Loan.objects.filter(user=user, deleted=False)
        software_costs = SoftwareCost.objects.filter(user=user, deleted=False)
        owner_equities = OwnerEquity.objects.filter(user=user, deleted=False)
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
    return bank_create(request)

def edit_bank(request, id):
    return bank_edit(request, id)

def delete_bank(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            bank = Bank.objects.get(pk=id)
            bank.deleted = True
            bank.deleted_at = DateFunction.now()
            bank.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def create_office(request):
    return office_create(request)

def edit_office(request, id):
    return office_edit(request, id)

def delete_office(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            office = Office.objects.get(pk=id)
            office.deleted = True
            office.deleted_at = DateFunction.now()
            office.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def create_staff(request):
    return staff_create(request)

def edit_staff(request, id):
    return staff_edit(request, id)

def delete_staff(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            staff = Staff.objects.get(pk=id)
            staff.deleted = True
            staff.deleted_at = DateFunction.now()
            staff.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def create_product(request):
    return product_create(request)

def edit_product(request, id):
    return product_edit(request, id)

def delete_product(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=id)
            product.deleted = True
            product.deleted_at = DateFunction.now()
            product.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})

def create_loan(request):
    return loan_create(request)

def edit_loan(request, id):
    return loan_edit(request, id)

def delete_loan(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            loan = Loan.objects.get(pk=id)
            loan.deleted = True
            loan.deleted_at = DateFunction.now()
            loan.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})

def create_software_cost(request):
    return software_cost_create(request)

def edit_software_cost(request, id):
    return software_cost_edit(request, id)

def delete_software_cost(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            software = SoftwareCost.objects.get(pk=id)
            software.deleted = True
            software.deleted_at = DateFunction.now()
            software.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def create_owner_equity(request):
    return owner_equity_create(request)

def edit_owner_equity(request, id):
    return owner_equity_edit(request, id)

def delete_owner_equity(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            equity = OwnerEquity.objects.get(pk=id)
            equity.deleted = True
            equity.deleted_at = DateFunction.now()
            equity.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})


