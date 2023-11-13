from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from user_onboard.models import User
from .forms import CreditorForm
from sales.models import Stakeholder
from django.http import JsonResponse


def index(request):
    try:
        user = User.objects.get(username=request.user)
        creditors = Stakeholder.objects.filter(user_id=user.user_id, type="Creditor")
    except Exception as e:
        return redirect('/')

    context = {
        'url': "/dashboard/creditors/",
        'creditors': creditors
    }
    return render(request, 'pages/index_creditors.html', context)


def create(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    form = CreditorForm()

    context = {
        'url': "/dashboard/vendor/",
        'edit': False,
        'form': form
    }

    if request.method == 'POST':
        form = CreditorForm(request.POST)

        if form.is_valid():

            try:
                new_stakeholder = Stakeholder(
                    customer_id=form.cleaned_data["customer_id"],
                    user_id=user,
                    name=form.cleaned_data["name"],
                    company=form.cleaned_data["company"],
                    email=form.cleaned_data["email"],
                    handphone=form.cleaned_data["phone"],
                    address=form.cleaned_data["address"],
                    delivery_address=form.cleaned_data["delivery_address"],
                    tax_information=form.cleaned_data["tax"],
                    website=form.cleaned_data["website"],
                    linkedin=form.cleaned_data["linkedIn"],
                    facebook=form.cleaned_data["facebook"],
                    tiktok=form.cleaned_data["tiktok"],
                    type="Creditor"
                )

                new_stakeholder.save()
                return redirect("/dashboard/creditors")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                context['form'] = form
                return render(request, 'pages/creditorform.html', context)

        else:

            context['form'] = form
            return render(request, 'pages/creditorform.html', context)

    return render(request, 'pages/creditorform.html', context)

def edit(request, id):
    vendor = Stakeholder.objects.get(pk=id)

    existing_data = {
        'customer_id':vendor.customer_id,
        'name': vendor.name,
        'company': vendor.company,
        'email':vendor.email,
        'phone': vendor.handphone, 
        'address': vendor.address,
        'delivery_address':vendor.delivery_address,
        'tax': vendor.tax_information,
        'website': vendor.website,
        'linkedIn': vendor.linkedin,
        'facebook': vendor.facebook,
        'tiktok': vendor.tiktok
    }

    form = CreditorForm(initial=existing_data)

    context = {
        'url': "/dashboard/vendor/",
        'edit': True,
        'form': form
    }

    if request.method == 'POST':
        form = CreditorForm(request.POST)

        if form.is_valid():
            try:
                vendor.customer_id = form.cleaned_data['customer_id']
                vendor.name= form.cleaned_data['name']
                vendor.company = form.cleaned_data['company']
                vendor.email = form.cleaned_data['email']
                vendor.handphone = form.cleaned_data['phone']
                vendor.address = form.cleaned_data['address']
                vendor.delivery_address = form.cleaned_data['delivery_address']
                vendor.tax_information = form.cleaned_data['tax']
                vendor.website = form.cleaned_data['website']
                vendor.linkedin = form.cleaned_data['linkedIn']
                vendor.facebook = form.cleaned_data['facebook']
                vendor.tiktok = form.cleaned_data['tiktok']

                vendor.save()
                return redirect("/dashboard/creditors")
            except Exception as e:

                error_message = str(e)
                form.add_error(None, error_message)
                context['form'] = form
                return render(request, 'pages/creditorform.html', context)

        else:
            context['form'] = form
            return render(request, 'pages/creditorform.html', context)

    return render(request, 'pages/creditorform.html', context)

def delete(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            vendor = Stakeholder.objects.get(pk=id)
            vendor.delete()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})
