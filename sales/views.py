from django.shortcuts import render
from .models import Sales,Customer,SalesLineItems,Product,ShippingInformation,SalesFooter
from .forms import SalesForm,CustomerForm,SalesLineItemsForm,ShippingForm,SalesLineItemswithIDForm
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

from .serializers import SalesSerializer, SalesLineItemsSerializer, SalesFooterSerializer, ShippingInformationSerializer
#SalesLineItemsFormSet = modelformset_factory(SalesLineItems, form=SalesLineItemsForm, extra=1)


@api_view(['POST'])
def create_sales_api(request):
    serializer = SalesSerializer(data=request.data)
    if serializer.is_valid():
        
        # Extract related data
        line_items_data = serializer.validated_data.pop('line_items', [])
        shipping_info_data = serializer.validated_data.pop('shipping_information', None)

        # Create Sales instance
        sales_instance = Sales.objects.create(**serializer.validated_data)

        # Create and link line items
        for item_data in line_items_data:
            SalesLineItems.objects.create(sales_id=sales_instance, **item_data)

        # Create and link shipping information
        if shipping_info_data:
            ShippingInformation.objects.create(sales_id=sales_instance, **shipping_info_data)

        return Response({"success": True}, status=status.HTTP_201_CREATED)
    else:
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def add_customer_api(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        name = data.get('name')
        customer_id = data.get('customer_id')
        company = data.get('company')
        email = data.get('email')
        handphone = data.get('handphone')
        address = data.get('address')
        delivery_address = data.get('delivery_address')
        tax_information = data.get('tax_information')
        website = data.get('website')
        linkedin = data.get('linkedin')
        facebook = data.get('facebook')
        tiktok = data.get('tiktok')

        if customer_id and name:
            customer = Customer(
                customer_id=customer_id,
                name=name,
                company=company,
                email=email,
                handphone=handphone,
                address=address,
                delivery_address=delivery_address,
                tax_information=tax_information,
                website=website,
                linkedin=linkedin,
                facebook=facebook,
                tiktok=tiktok
            )
            customer.save()
            return JsonResponse({"success": True}, status=201)
        else:
            return JsonResponse({"success": False, "error": "Customer ID and Name fields are required"}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request method"}, status=400)


def sales_dashboard(request):
    sales = Sales.objects.annotate(total_amount=Sum('line_items__total_price'))
    sales_line_data = SalesLineItems.objects.all()


    context = {
        'url': "/dashboard/sales",
        'sales_data': sales,
        'sales_line_data': sales_line_data,
    }
    print(context)
    return render(request, 'sales/sales_dashboard.html', context)



def generate_quotation(request, sales_id):
    # Fetch the sale data
    sale = Sales.objects.get(sales_id=sales_id)
    sale_lines = SalesLineItems.objects.filter(sales_id=sales_id)
    
    # Use a PDF generation library to generate the PDF
    # Here's a pseudo-code for it, you might use libraries like ReportLab, xhtml2pdf, WeasyPrint, etc.
    pdf = generatedoc.generate_professional_pdf_from_sale(sale,sale_lines) # This function should return the binary data for the PDF

    # Return the PDF as a response
    response = FileResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="quotation_{sales_id}.pdf"'
    
    return response

def create_sales(request):
    # Define the formset class
    SalesLineItemsFormSet = modelformset_factory(SalesLineItems, form=SalesLineItemsForm, extra=1)
    all_products = serialize('json', Product.objects.all())
    if request.method == 'POST':
        form = SalesForm(request.POST)
        formset = SalesLineItemsFormSet(request.POST, prefix="lineitems")
        shipform = ShippingForm(request.POST)

        print(shipform.errors)
        if form.is_valid() and formset.is_valid() and shipform.is_valid():
            sales_instance = form.save(commit=False)
            print(form.cleaned_data)
            sales_instance.user_id = request.user
            sales_instance.save()

            # Save each form in the formset
            for item_form in formset:
                item_instance = item_form.save(commit=False)
                item_instance.sales_id = sales_instance
                item_instance.save()

            ship_instance = shipform.save(commit=False)
            ship_instance.sales_id = sales_instance
            ship_instance.save()
            
            # You should redirect after successful POST (PRG pattern)
            return redirect("/sales")
        else:
            messages.error(request, 'Failed to create sales entry. Please correct the errors below.')
    else:
        form = SalesForm()
        formset = SalesLineItemsFormSet(queryset=SalesLineItems.objects.none(), prefix="lineitems")
        shipform = ShippingForm(request.POST)

    return_value = {
        'url': "/dashboard/sales",
        'form': form,
        "formset": formset,
        "shipform":shipform,
        'all_products':all_products
    }

    return render(request, 'sales/create_sales.html', return_value)


def add_customer(request):
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"success": True})
            else:
                # Return the form errors in the response if needed
                return JsonResponse({"success": False, "errors": form.errors})
        return JsonResponse({"success": False, "error": "Invalid request method"})


def get_customer_data(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
        data = {
            "address": customer.address,
            "delivery_address": customer.delivery_address,
        }
        return JsonResponse(data)
    except Customer.DoesNotExist:
        return JsonResponse({}, status=404)


def delete_sales(request, sales_id):
    try:
        sale = Sales.objects.get(pk=sales_id)
        
        # Delete related SalesLine items
        SalesLineItems.objects.filter(sales_id=sale).delete()
        
        # Delete related Shipping records
        ShippingInformation.objects.filter(sales_id=sale).delete()
        
        # Delete related Footer records
        SalesFooter.objects.filter(sales_id=sale).delete()
        
        # Finally, delete the Sales record
        sale.delete()

        # Optionally, add a message using Django's messages framework to inform user of successful delete.

    except Sales.DoesNotExist:
        # Handle the error, e.g. show a 404 error page, or redirect back with an error message.
        pass
    
    return redirect('sales_dashboard')

def delete_sales_line(request, sales_line_id):
    try:
        sale_line = SalesLineItems.objects.get(pk=sales_line_id)
        
        
        sale_line.delete()

        # Optionally, add a message using Django's messages framework to inform user of successful delete.

    except SalesLineItems.DoesNotExist:
        # Handle the error, e.g. show a 404 error page, or redirect back with an error message.
        pass
    
    return redirect('sales_dashboard')   


def edit_sales(request, sales_id):
    # Fetch the existing sales instance
    existing_sale = get_object_or_404(Sales, sales_id=sales_id)

    # Define the formset class
    SalesLineItemsFormSet = modelformset_factory(SalesLineItems, form=SalesLineItemswithIDForm,extra=0)
    all_products = serialize('json', Product.objects.all())

    if request.method == 'POST':
        form = SalesForm(request.POST, instance=existing_sale)
        formset = SalesLineItemsFormSet(request.POST, prefix="lineitems", queryset=SalesLineItems.objects.filter(sales_id=existing_sale))
        shipform = ShippingForm(request.POST, instance=ShippingInformation.objects.get(sales_id=existing_sale))
        print(form.is_valid())
        print(formset.errors)
        print(shipform.is_valid())

        if form.is_valid() and formset.is_valid() and shipform.is_valid():
            sales_instance = form.save()
            #print(request.POST)
            # Update line items
            for item_form in formset:
                item_instance = item_form.save(commit=False)
                item_instance.sales_id = sales_instance
                item_instance.product_id = item_form.cleaned_data.get('product_id')
                print(item_instance)
                item_instance.save()

            # Update shipping details
            ship_instance = shipform.save()

            return redirect("/sales")
        else:
            messages.error(request, 'Failed to update sales entry. Please correct the errors below.')

    else:
        form = SalesForm(instance=existing_sale)
        formset = SalesLineItemsFormSet(prefix="lineitems", queryset=SalesLineItems.objects.filter(sales_id=existing_sale))
        shipform = ShippingForm(instance=ShippingInformation.objects.get(sales_id=existing_sale))

    return_value = {
        'url': "/dashboard/sales",
        'form': form,
        "formset": formset,
        "shipform": shipform,
        'all_products': all_products
    }

    return render(request, 'sales/edit_template.html', return_value)

def edit_sales_line(request, sales_id):
    sale = get_object_or_404(Sales, id=sales_id)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sales')
    else:
        form = SalesForm(instance=sale)
    return render(request, 'sales/edit_template.html', {'form': form})