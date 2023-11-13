from django.shortcuts import render, redirect
from user_onboard.models import User, Address, Office
from user_onboard.accounts_forms import OfficeForm


def office_create(request):
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
                    existing_address = Address.objects.get(
                        pk=form.cleaned_data['address'])
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
                return render(request, 'pages/formPages/office_page.html', {'form': form, 'edit': False})
        else:
            form = OfficeForm(request, dynamic_choices=choices_list)

    return render(request, 'pages/formPages/office_page.html', {'form': form, 'edit': False})


def office_edit(request, id):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
        office = Office.objects.get(pk=id)
    except Exception as e:
        return redirect('/')

    existing_data = {
        'name': office.name,
        'address': office.address.address_id,
        'rent': office.rent,
        'electric': office.electric,
        'water': office.water,
        'internet': office.internet,
        'rental': office.rental,
        'rental_deposit': office.rental_deposit,
        'create_new_address': False
    }

    choices_list = [(address.address_id, address) for address in addresses]

    form = OfficeForm(dynamic_choices=choices_list, initial=existing_data)

    if request.method == 'POST':
        form = OfficeForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():
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

                    office.name = form.cleaned_data['name'],
                    office.address = new_address,
                    office.rent = form.cleaned_data['rent'],
                    office.electric = int(
                        form.cleaned_data['electric']) if form.cleaned_data['electric'] else 0,
                    office.water = int(form.cleaned_data['water']
                                       ) if form.cleaned_data['water'] else 0,
                    office.internet = int(
                        form.cleaned_data['internet']) if form.cleaned_data['internet'] else 0,
                    office.rental = int(form.cleaned_data['rental']
                                        ) if form.cleaned_data['rental'] else 0,
                    office.rental_deposit = int(
                        form.cleaned_data['rental_deposit']) if form.cleaned_data['rental_deposit'] else 0,

                    office.save()

                    return redirect("/dashboard/account-setup")
                else:
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])
                    print("\n\n")
                    print(existing_address.city)
                    office.name = form.cleaned_data['name']
                    office.address = existing_address

                    office.rent = form.cleaned_data['rent']
                    office.electric = int(
                        form.cleaned_data['electric']) if form.cleaned_data['electric'] else 0
                    office.water = int(form.cleaned_data['water']
                                       ) if form.cleaned_data['water'] else 0
                    office.internet = int(
                        form.cleaned_data['internet']) if form.cleaned_data['internet'] else 0
                    office.rental = int(form.cleaned_data['rental']
                                        ) if form.cleaned_data['rental'] else 0
                    office.rental_deposit = int(
                        form.cleaned_data['rental_deposit']) if form.cleaned_data['rental_deposit'] else 0

                    office.save()

                    return redirect("/dashboard/account-setup")

            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/office_page.html', {'form': form, 'edit': True})
        else:
            form = OfficeForm(request, dynamic_choices=choices_list)

    return render(request, 'pages/formPages/office_page.html', {'form': form, 'edit': True})
