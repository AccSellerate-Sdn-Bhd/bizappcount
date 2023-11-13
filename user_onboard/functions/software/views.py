from django.shortcuts import render, redirect
from user_onboard.models import User, SoftwareCost
from user_onboard.accounts_forms import SoftwareCostForm

def software_cost_create(request):
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

def software_cost_edit(request, id):
    try:
        software = SoftwareCost.objects.get(pk=id)
    except Exception as e:
        return redirect('/')
    
    existing_data = {
      'name': software.name,
      'type': software.type,
      'software_billing_info': software.software_billing_info,
      'company_name': software.company_name,
      'billing_duration': software.billing_duration,
      'amount': software.amount,
      'active': software.active,
    }

    form = SoftwareCostForm(initial=existing_data)

    if request.method == 'POST':
        form = SoftwareCostForm(request.POST)

        if form.is_valid():
            try:

                software.name = form.cleaned_data['name']
                software.type = form.cleaned_data['type']
                software.software_billing_info = form.cleaned_data['software_billing_info']
                software.company_name = form.cleaned_data['company_name']
                software.billing_duration = form.cleaned_data['billing_duration']
                software.amount = form.cleaned_data['amount']
                software.active = form.cleaned_data['active']
                

                software.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/software_page.html', {'form': form, 'edit': True})
        else:
            print(form.errors)
            form = SoftwareCostForm(request.POST)
 
    return render(request, 'pages/formPages/software_page.html', {'form': form, 'edit': True})

