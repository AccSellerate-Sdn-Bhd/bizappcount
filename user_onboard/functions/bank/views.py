from django.shortcuts import render, redirect
from user_onboard.models import User, Address, Bank
from user_onboard.accounts_forms import BankForm


def bank_create(request):
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
                if (form.cleaned_data['create_new_address']):
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
                    existing_address = Address.objects.get(
                        pk=form.cleaned_data['address'])

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
                return render(request, 'pages/formPages/bank_page.html', {'form': form, 'edit': False})

        else:
            return render(request, 'pages/formPages/bank_page.html', {'form': form, 'edit': False})
    else:
        return render(request, 'pages/formPages/bank_page.html', {'form': form, 'edit': False})


def bank_edit(request, id):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
        bank = Bank.objects.get(pk=id)
    except Exception as e:
        return redirect('/')

    existing_data = {
        'name': bank.name,
        'account_no': bank.account_no,
        'type': bank.type,
        'bizapp': bank.bizapp,
        'address': bank.address.address_id,
        'create_new_address': False
    }

    choices_list = [(address.address_id, address) for address in addresses]

    form = BankForm(dynamic_choices=choices_list, initial=existing_data)

    if request.method == 'POST':
        form = BankForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():
            print(form.cleaned_data['create_new_address'])

            try:
                if (form.cleaned_data['create_new_address']):
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

                    bank.name = form.cleaned_data['name']
                    bank.account_no = form.cleaned_data['account_no']
                    bank.address = new_address
                    bank.type = form.cleaned_data['type']
                    bank.bizapp = form.cleaned_data['bizapp']

                    bank.save()

                    return redirect("/dashboard/account-setup")
                else:
                    print(form.cleaned_data['address'])
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])

                    bank.name = form.cleaned_data['name']
                    bank.account_no = form.cleaned_data['account_no']
                    bank.address=existing_address
                    bank.type = form.cleaned_data['type']
                    bank.bizapp = form.cleaned_data['bizapp']

                    bank.save()

                    return redirect("/dashboard/account-setup")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/bank_page.html', {'form': form, 'edit': True})

        else:
            return render(request, 'pages/formPages/bank_page.html', {'form': form, 'edit': True})
    else:
        return render(request, 'pages/formPages/bank_page.html', {'form': form, 'edit': True})
