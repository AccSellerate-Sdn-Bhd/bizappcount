from django.shortcuts import render, redirect
from user_onboard.models import User, Product
from user_onboard.accounts_forms import ProductForm

def product_create(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')
    
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            try:
                new_product = Product(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    brand = form.cleaned_data['brand'],
                    collection = form.cleaned_data['collection'],
                    SKU = form.cleaned_data['SKU'],
                    barcode = form.cleaned_data['barcode'],
                    weight = int(form.cleaned_data['weight']) if form.cleaned_data['weight'] else None,
                    height = int(form.cleaned_data['height']) if form.cleaned_data['height'] else None,
                    width = int(form.cleaned_data['width']) if form.cleaned_data['width'] else None,
                    length = int(form.cleaned_data['length']) if form.cleaned_data['length'] else None,
                    cost = form.cleaned_data['cost'],
                    forex = form.cleaned_data['forex'],
                    retail_selling_price = form.cleaned_data['retail_selling_price'],
                    status = form.cleaned_data['status'],
                    user=user
                )

                new_product.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/product_page.html', {'form': form})
        else:
            print(form.errors)
            form = ProductForm(request.POST)
 
    return render(request, 'pages/formPages/product_page.html', {'form': form})

def product_edit(request, id):
    try:
        user = User.objects.get(username=request.user)
        product = Product.objects.get(pk=id)
    except Exception as e:
        return redirect('/')
    
    existing_data = {
        'name': product.name,
        'description':product.description,
        'brand': product.brand,
        'collection': product.collection,
        'SKU': product.SKU,
        'barcode': product.barcode,
        'weight': product.weight,
        'height': product.height,
        'width': product.width,
        'length': product.length,
        'cost':product.cost,
        'forex':product.forex,
        'retail_selling_price': product.retail_selling_price,
        'status': product.status
    }

    form = ProductForm(initial=existing_data)

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            try:

                product.name = form.cleaned_data['name']
                product.description = form.cleaned_data['description']
                product.brand = form.cleaned_data['brand']
                product.collection = form.cleaned_data['collection']
                product.SKU = form.cleaned_data['SKU']
                product.barcode = form.cleaned_data['barcode']
                product.weight = int(form.cleaned_data['weight']) if form.cleaned_data['weight'] else None
                product.height = int(form.cleaned_data['height']) if form.cleaned_data['height'] else None
                product.width = int(form.cleaned_data['width']) if form.cleaned_data['width'] else None
                product.length = int(form.cleaned_data['length']) if form.cleaned_data['length'] else None
                product.cost = form.cleaned_data['cost']
                product.forex = form.cleaned_data['forex']
                product.retail_selling_price = form.cleaned_data['retail_selling_price']
                product.status = form.cleaned_data['status']


                product.save()

                return redirect("/dashboard/account-setup")
                
            except Exception as e:
                error_message = str(e)
                form.add_error(None, error_message)
                return render(request, 'pages/formPages/product_page.html', {'form': form, 'edit': True})
        else:
            print(form.errors)
            form = ProductForm(request.POST)
 
    return render(request, 'pages/formPages/product_page.html', {'form': form, 'edit': True})