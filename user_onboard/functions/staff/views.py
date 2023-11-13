from django.shortcuts import render, redirect
from user_onboard.models import User, Address, Staff
from user_onboard.accounts_forms import StaffForm

def staff_create(request):
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
                return render(request, 'pages/formPages/staff_page.html', {'form': form, 'edit': False})
        else:
            form = StaffForm(request, dynamic_choices=choices_list)
 
    return render(request, 'pages/formPages/staff_page.html', {'form': form, 'edit': False})

def staff_edit(request, id):
    try:
        user = User.objects.get(username=request.user)
        addresses = Address.objects.filter(user=user)
        staff = Staff.objects.get(pk=id)
    except Exception as e:
        return redirect('/')

    existing_data = {
        'name': staff.name,
        'address': staff.address.address_id,
        'ic_passport': staff.ic_passport,
        'type': staff.type,
        'phone_no': staff.phone_no,
        'date_joined': staff.date_joined,
        'position': staff.position,
        'salary': staff.salary,
        'epf': staff.epf,
        'create_new_address': False
    }

    choices_list = [(address.address_id, address) for address in addresses]

    form = StaffForm(dynamic_choices=choices_list, initial=existing_data)

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

                    staff.name=form.cleaned_data['name']
                    staff.address=new_address
                    staff.ic_passport = form.cleaned_data['ic_passport']
                    staff.type = form.cleaned_data['type']
                    staff.phone_no = form.cleaned_data['phone_no']
                    staff.date_joined = form.cleaned_data['date_joined']
                    staff.position = form.cleaned_data['position']
                    staff.salary = float(form.cleaned_data['salary'])
                    staff.epf = float(form.cleaned_data['epf'])
                    

                    staff.save()

                    return redirect("/dashboard/account-setup")
                else:
                    existing_address = Address.objects.get(pk=form.cleaned_data['address'])
                    
                    staff.name=form.cleaned_data['name']
                    staff.address=existing_address
                    staff.ic_passport = form.cleaned_data['ic_passport']
                    staff.type = form.cleaned_data['type']
                    staff.phone_no = form.cleaned_data['phone_no']
                    staff.date_joined = form.cleaned_data['date_joined']
                    staff.position = form.cleaned_data['position']
                    staff.salary = float(form.cleaned_data['salary'])
                    staff.epf = float(form.cleaned_data['epf'])

                    staff.save()

                    return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/staff_page.html', {'form': form, 'edit': True})
        else:
            form = StaffForm(request, dynamic_choices=choices_list)
 
    return render(request, 'pages/formPages/staff_page.html', {'form': form, 'edit': True})