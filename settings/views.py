from django.shortcuts import render
from sales.models import Customer
from .forms import CustomerForm
from user_onboard.models import User, Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.http import FileResponse
import generatedoc
from django.shortcuts import redirect,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


#SalesLineItemsFormSet = modelformset_factory(SalesLineItems, form=SalesLineItemsForm, extra=1)
@login_required
def customer_dashboard(request):

    user = User.objects.get(username=request.user)
    customer = Customer.objects.filter(user_id=user)

    context = {
        'url': "/settings/customer",
        'customer_data': customer
    }
    print(context)
    return render(request, 'settings/customer_dashboard.html', context)

@login_required
def create_customer(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')
    # Define the formset class
    if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                customer_instance = form.save(commit=False)
                print(form.cleaned_data)
                customer_instance.user_id = request.user
                customer_instance.save()

                return redirect("/dashboard/settings/customer")
            else:
                messages.error(request, 'Failed to create customer. Please correct the errors below.')
    else:
        form = CustomerForm(request.POST)

    return_value = {
        'url': "/settings/customer",
        'form': form
    }

    return render(request, 'settings/create_customer.html', return_value)


@login_required
def delete_customer(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
        
        customer.delete()

        # Optionally, add a message using Django's messages framework to inform user of successful delete.

    except Customer.DoesNotExist:
        # Handle the error, e.g. show a 404 error page, or redirect back with an error message.
        pass
    
    return redirect("/dashboard/settings/customer")

@login_required
def edit_customer(request, customer_id):
    try:
        user = User.objects.get(username=request.user)
    except User.DoesNotExist:
        return redirect('/')

    # Get the customer instance
    customer_instance = get_object_or_404(Customer, pk=customer_id, user_id=user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully.')
            return redirect('/dashboard/settings/customer')
        else:
            messages.error(request, 'Failed to update customer. Please correct the errors below.')
    else:
        # If not POST, create the form with the customer instance
        form = CustomerForm(instance=customer_instance)

    return render(request, 'settings/edit_customer.html', {
        'url': '/settings/customer',
        'form': form,
        'edit': True,  # You can use this to toggle between save or update in your template
    })