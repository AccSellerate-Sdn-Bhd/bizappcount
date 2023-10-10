from django.shortcuts import render, redirect
from user_onboard.models import User, Product
from .models import Inventory, InventoryHistory
from .forms import InventoryForm
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
# Create your views here.


def index(request):
    try:
        user = User.objects.get(username=request.user)
        inventory = Inventory.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    context = {
        'url': "/dashboard/inventory/",
        'inventory': inventory
    }
    return render(request, 'pages/index.html', context)


def create(request):
    try:
        user = User.objects.get(username=request.user)
        products = Product.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    print('\n')
    print("alone")
    print(products)

    choices_list = [(product.product_id, product) for product in products]
    form = InventoryForm(dynamic_choices=choices_list)

    if request.method == 'POST':
        form = InventoryForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():

            try:
                existing_product = Product.objects.get(
                    pk=form.cleaned_data['product'])

                new_inventory = Inventory(
                    user=user,
                    product=existing_product,
                    name=form.cleaned_data['name'],
                    amount=form.cleaned_data['amount'],
                    unit=form.cleaned_data['unit'],
                    price_per_unit=form.cleaned_data['price_per_unit'],
                )

                new_inventory_history = InventoryHistory(
                    inventory=new_inventory,
                    description="Created new inventory",
                    increase=True,
                    amount=form.cleaned_data['amount']
                )

                new_inventory.save()
                new_inventory_history.save()

                return redirect("/dashboard/inventory")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/inventoryform.html', {'form': form, 'url': "/dashboard/inventory"})

        else:
            return render(request, 'pages/inventoryform.html', {'form': form, 'url': "/dashboard/inventory"})
    else:
        return render(request, 'pages/inventoryform.html', {'form': form, 'url': "/dashboard/inventory"})


def edit(request, id):
    try:
        user = User.objects.get(username=request.user)
        products = Product.objects.filter(user=user)
        inventory = Inventory.objects.get(pk=id)
    except Exception as e:
        return redirect('/')

    choices_list = [(product.product_id, product) for product in products]
    existing_data = {
        'name': inventory.name,
        'amount': inventory.amount,
        'unit': inventory.unit,
        'price_per_unit': inventory.price_per_unit,
        'product': inventory.product.product_id
    }

    form = InventoryForm(dynamic_choices=choices_list, initial=existing_data)

    if request.method == 'POST':
        form = InventoryForm(request.POST, dynamic_choices=choices_list)

        if form.is_valid():

            try:
                existing_product = Product.objects.get(
                    pk=form.cleaned_data['product'])
                
                difference = float(form.cleaned_data['amount']) - float(inventory.amount)

                functionResult = getDifference(inventory, form, existing_product)

                print("Clicked")
                print(functionResult['editedFields'], functionResult['newInventory'])
                if(len(functionResult['editedFields']) > 0):
                    editedFieldsString = ', '.join(functionResult['editedFields'])

                    if (difference < 0):
                        increase = False
                        amount = abs(difference)
                    else:
                        increase = True
                        amount = difference

                    print("\n a lot of heart")
                    print(amount)

                    new_inventory_history = InventoryHistory(
                        inventory=inventory,
                        description="Edited inventory, fields changed: " + editedFieldsString,
                        increase=increase,
                        amount=amount
                    )

                    functionResult['newInventory'].save()
                    new_inventory_history.save()

                return redirect("/dashboard/inventory")
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/inventoryform.html', {'form': form, 'url': "/dashboard/inventory", 'edit': True})

        else:
            return render(request, 'pages/inventoryform.html', {'form': form, 'url': "/dashboard/inventory", 'edit': True})
    else:
        return render(request, 'pages/inventoryform.html', {'form': form, 'url': "/dashboard/inventory", 'edit': True})

def getDifference(inventory, form, existing_product):
    editedFields = []
    if not (inventory.name == form.cleaned_data['name']):
        editedFields.append("name")
        inventory.name = form.cleaned_data['name']

    if not (inventory.product == existing_product):
        editedFields.append("product")
        inventory.product = existing_product

    if not (float(inventory.amount) == float(form.cleaned_data['amount'])):
        editedFields.append("amount")
        inventory.amount = form.cleaned_data['amount']
        
    if not (inventory.unit == form.cleaned_data['unit']):
        editedFields.append("unit")
        inventory.unit = form.cleaned_data['unit']

    if not (float(inventory.price_per_unit) == float(form.cleaned_data['price_per_unit'])):
        editedFields.append("Price per unit")
        inventory.price_per_unit = form.cleaned_data['price_per_unit']
    
    return {'editedFields': editedFields, 'newInventory': inventory}

def history(request, id):
    try:
        inventory = Inventory.objects.get(pk=id)
        histories = InventoryHistory.objects.filter(inventory=inventory)
    except Exception as e:
        return redirect('/')

    return render(request, 'pages/history.html', {'histories': histories,  'url': "/dashboard/inventory"})


def delete(request, id):
    print("delete the following")
    print(id)
    if request.method == 'DELETE':
        try:
            inventory = Inventory.objects.get(pk=id)
            inventory.delete()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": e})

    return JsonResponse({"success": False, "error": "Invalid request method"})
