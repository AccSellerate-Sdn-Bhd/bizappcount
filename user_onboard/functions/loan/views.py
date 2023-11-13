from django.shortcuts import render, redirect
from user_onboard.models import User, Address, Loan
from user_onboard.accounts_forms import LoanForm

def loan_create(request):
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

def loan_edit(request, id):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
        loan = Loan.objects.get(pk=id)
    except Exception as e:
        return redirect('/')

    existing_data = {
        'name': loan.name,
        'category': loan.category,
        'creditor': loan.creditor,
        'address': loan.creditor_address.address_id,
        'creditor_phone_no': loan.creditor_phone_no,
        'amount': loan.amount,
        'amount_payable': loan.amount_payable,
        'interest': loan.interest,
        'installment_amount': loan.installment_amount,
        'not_defined': loan.not_defined,
        'recurring': loan.recurring,
        'active': loan.active,
    }

    choices_list = [(address.address_id, address) for address in addresses]

    form = LoanForm(dynamic_choices=choices_list, initial=existing_data)

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


                    loan.name = form.cleaned_data['name'],
                    loan.category = form.cleaned_data['category'],
                    loan.creditor = form.cleaned_data['creditor'],
                    loan.creditor_address = new_address,
                    loan.creditor_phone_no = form.cleaned_data['creditor_phone_no'],
                    
                    loan.amount = form.cleaned_data['amount'],
                    loan.amount_payable = form.cleaned_data['amount_payable'],
                    loan.interest = form.cleaned_data['interest'],
                    loan.installment_amount = form.cleaned_data['installment_amount'],
                    loan.not_defined = form.cleaned_data['not_defined'],
                    loan.recurring = form.cleaned_data['recurring'],
                    loan.active = form.cleaned_data['active'],
                        

                    loan.save()

                    return redirect("/dashboard/account-setup")
                else:
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])
                    

                    loan.name = form.cleaned_data['name']
                    loan.category = form.cleaned_data['category']
                    loan.creditor = form.cleaned_data['creditor']
                    loan.creditor_address = existing_address
                    loan.creditor_phone_no = form.cleaned_data['creditor_phone_no']
                    
                    loan.amount = form.cleaned_data['amount']
                    loan.amount_payable = form.cleaned_data['amount_payable']
                    loan.interest = form.cleaned_data['interest']
                    loan.installment_amount = form.cleaned_data['installment_amount']
                    loan.not_defined = form.cleaned_data['not_defined']
                    loan.recurring = form.cleaned_data['recurring']
                    loan.active = form.cleaned_data['active']
                        

                    loan.save()

                    return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/loan_page.html', {'form': form, 'edit': True})
        else:
            form = LoanForm(request, dynamic_choices=choices_list)
 
    return render(request, 'pages/formPages/loan_page.html', {'form': form, 'edit': True})