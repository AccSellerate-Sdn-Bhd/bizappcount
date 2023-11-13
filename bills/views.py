from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from user_onboard.models import User
from .forms import BillForm
from .models import Bill
from django.http import JsonResponse
from datetime import datetime as DateFunction


def index(request):
    try:
        user = User.objects.get(username=request.user)
        bills = Bill.objects.filter(user_id=user.user_id)
    except Exception as e:
        return redirect('/')

    context = {
        'url': "/dashboard/bills/",
        'bills': bills
    }
    return render(request, 'pages/index_bills.html', context)


def create(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    form = BillForm()

    context = {
        'url': "/dashboard/bills/",
        'edit': False,
        'form': form
    }

    if request.method == 'POST':
        form = BillForm(request.POST)

        if form.is_valid():
            currentime = DateFunction.now()
            try:
                new_stakeholder = Bill(
                    user=user,
                    name=form.cleaned_data['name'],
                    amount=form.cleaned_data['amount'],
                    interval=form.cleaned_data['recurring_interval'],
                    datetime = currentime
                )

                new_stakeholder.save()
                return redirect("/dashboard/bills")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                context['form'] = form
                return render(request, 'pages/billform.html', context)

        else:

            context['form'] = form
            return render(request, 'pages/billform.html', context)

    return render(request, 'pages/billform.html', context)

def edit(request, id):
    bill = Bill.objects.get(pk=id)

    existing_data = {
        'name': bill.name,
        'amount': bill.amount,
        'recurring_interval':bill.interval,
    }

    form = BillForm(initial=existing_data)

    context = {
        'url': "/dashboard/vendor/",
        'edit': True,
        'form': form
    }

    if request.method == 'POST':
        form = BillForm(request.POST)

        if form.is_valid():
            try:
                bill.name= form.cleaned_data['name']
                bill.amount = form.cleaned_data['amount']
                bill.interval = form.cleaned_data['recurring_interval']
      

                bill.save()
                return redirect("/dashboard/bills")
            except Exception as e:

                error_message = str(e)
                form.add_error(None, error_message)
                context['form'] = form
                return render(request, 'pages/billform.html', context)

        else:
            context['form'] = form
            return render(request, 'pages/billform.html', context)

    return render(request, 'pages/billform.html', context)

def delete(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            vendor = Bill.objects.get(pk=id)
            vendor.delete()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})
