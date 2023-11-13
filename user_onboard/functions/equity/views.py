from django.shortcuts import render, redirect
from user_onboard.models import User, OwnerEquity
from user_onboard.accounts_forms import OwnerEquityForm

def owner_equity_create(request):
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

def owner_equity_edit(request, id):
    try:
        equity = OwnerEquity.objects.get(pk=id)
    except Exception as e:
        return redirect('/')

    existing_data = {
      'name': equity.name,
      'ic_passport': equity.ic_passport,
      'nationality': equity.nationality,
      'bumiputera': equity.bumiputera,
      'percentage_ownership': equity.percentage_ownership,
      'paid_up_capital': equity.paid_up_capital,
    }
    
    form = OwnerEquityForm(initial=existing_data)

    if request.method == 'POST':
        form = OwnerEquityForm(request.POST)

        if form.is_valid():
            try:
                equity.name = form.cleaned_data['name']
                equity.ic_passport = form.cleaned_data['ic_passport']
                equity.nationality = form.cleaned_data['nationality']
                equity.bumiputera = form.cleaned_data['bumiputera']
                equity.percentage_ownership = form.cleaned_data['percentage_ownership']
                equity.paid_up_capital = form.cleaned_data['paid_up_capital']
                

                equity.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/equity_page.html', {'form': form, 'edit': True})
        else:
            print(form.errors)
            form = OwnerEquityForm(request.POST)
 
    return render(request, 'pages/formPages/equity_page.html', {'form': form, 'edit': True})