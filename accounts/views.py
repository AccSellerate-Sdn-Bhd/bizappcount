from django.shortcuts import render, redirect
from user_onboard.models import User
from report.models import AccountUserRelationship, Account
from .forms import AccountForm

def index(request):
    try:
        user = User.objects.get(username=request.user)
        accounts = AccountUserRelationship.objects.filter(user_id=user.user_id)
    except Exception as e:
        return redirect('/')

    context = {
        'url': "/dashboard/accounts/",
        'accounts': accounts
    }
    return render(request, 'pages/index_accounts.html', context)

def create(request):
    try:
        user = User.objects.get(username=request.user)
        accounts = Account.objects.filter(parent_acc_id=None)
    except Exception as e:
        return redirect('/')

    choices_list = [(None, 'No Parent Account')] 
    choices_list += [(account.account_id, account.name) for account in accounts]

    form =  AccountForm(dynamic_choices=choices_list)

    if request.method == 'POST':
        form = AccountForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():

            try:
                name = form.cleaned_data['name']
                account = form.cleaned_data['account']
                amount = form.cleaned_data['amount']
                print("\n\n")
                print(name, account, amount)

                if account == "":
                    new_account = Account.objects.create(
                        name=name,
                        type=name.lower(),
                    )
                    AccountUserRelationship.objects.create(
                        user=user,
                        account=new_account,
                        amount= float(amount)
                    )
                else:
                    parent_account = Account.objects.get(pk=account)

                    new_account = Account.objects.create(
                        name=name,
                        type=parent_account.name.lower(),
                        parent_acc=parent_account
                    )

                    AccountUserRelationship.objects.create(
                        user=user,
                        account=new_account,
                        amount= float(amount)
                    )

                return redirect("/dashboard/accounts")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/create_accounts.html', {'form': form, 'url': "/dashboard/accounts/"})

        else:
            return render(request, 'pages/create_accounts.html', {'form': form, 'url': "/dashboard/accounts/"})
    else:
        return render(request, 'pages/create_accounts.html', {'form': form, 'url': "/dashboard/accounts/"})