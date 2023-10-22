from django.shortcuts import render, redirect
from user_onboard.models import User, Product
from inventory.models import Inventory, InventoryHistory
from django.http import JsonResponse, HttpResponse
import io
from django.http import FileResponse
from report.models import Journal, Ledger, AccountUserRelationship
from django.db.models import F
from django.db.models import Count
from operator import itemgetter

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import datetime as DateFunction
from django.core import serializers
from io import BytesIO

# Create your views here.


def pandlreports(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    accounts = AccountUserRelationship.objects.filter(user=user.user_id)
    # print(ledgers, len(ledgers))

    data = []
    total = 0

    if (len(accounts) > 0):
        types = []
        for useraccount in accounts:
            print(useraccount.account.type)

            if useraccount.account.type in types:
                type_object = next((item for item in data if item["title"] == useraccount.account.type), None)
                new_array = type_object["data"]
                new_array.append(useraccount)
                type_object["data"] = new_array

            else:
                types.append(useraccount.account.type)
                newObject = {
                    "title": useraccount.account.type,
                    "data": [useraccount]
                }
                data.append(newObject)
            
            total = total + useraccount.amount
        
    print(data)

    return render(request, 'pages/pandlReports.html', {"url": "/dashboard/reports/profit-and-loss", "data": data, "total": total})


def getpandlreportsdata(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    journals = Journal.objects.filter(editable=1, user=user.user_id)
    currentime = DateFunction.now()

    balance = 0

    for journal in journals:
        print(journal)
        balance = balance - \
            float(journal.credit_amount) if journal.debit_amount == None else balance + \
            float(journal.debit_amount)

        ledger = Ledger(
            account=journal.account,
            journal=journal,
            user=user,
            datetime=currentime,
            name=journal.name,
            description=journal.description,
            debit_amount=journal.debit_amount,
            credit_amount=journal.credit_amount,
            balance=balance
        )

        useraccount = AccountUserRelationship.objects.filter(user=user.user_id, account=journal.account.account_id)
        if(len(useraccount)>0):
            olduseraccount = useraccount.first()

            new_amount= float(olduseraccount.amount) - float(journal.credit_amount) if journal.debit_amount == None else float(olduseraccount.amount) +  journal.debit_amount
            olduseraccount.amount = new_amount
            olduseraccount.save()
        else:
            newuseraccount = AccountUserRelationship(
                user=user,
                account=journal.account,
                amount= -float(journal.credit_amount) if journal.debit_amount == None else journal.debit_amount
            )
            newuseraccount.save()

        journal.editable = 0
        journal.save()
        ledger.save()

    return redirect('/dashboard/reports/profit-and-loss')


def generate_profit_and_loss_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Add the text "testing pdf" to the PDF
    p.drawString(100, 750, "Testing PDF")

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def balancesheetreports(request):
    return render(request, 'pages/balancesheetReports.html', {"url": "/dashboard/reports/balance-sheet"})


def generate_balance_sheet_report(request):
    # Create a PDF document
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create a list to hold the content
    elements = []

    # Your data for the table
    data = [
        ["Item", "Value"],
        ["Asset 1", "$1000"],
        ["Asset 2", "$2000"],
        ["Liability 1", "$500"],
        ["Liability 2", "$300"],
        ["Net Worth", "$2200"]
    ]

    # Create a table with the data
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # Build the PDF document
    doc.build(elements)

    # Reset the buffer to the beginning
    buffer.seek(0)

    # Create a response with PDF content type and attachment header
    response = FileResponse(buffer, as_attachment=True,
                            filename="balance_sheet.pdf")

    return response


def cashflowreports(request):

    display_data = processDataCashFlow()

    return render(request, 'pages/cashflowReports.html', {
        "url": "/dashboard/reports/cash-flow",
        'display_data': display_data
    })


def processDataCashFlow():
    data = []

    # Cash received
    cashreceived = []
    cashreceived.append(["name", 0, 0, 0])
    cashreceived.append(["name 2", 0, 0, 0])
    data.append(cashreceived)

    # Expenditures
    expenditures = []
    expenditures.append(["name", 0, 0, 0])
    expenditures.append(["name 2", 0, 0, 0])
    data.append(expenditures)

    return data


def generate_cash_flow_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Add the text "testing pdf" to the PDF
    p.drawString(100, 750, "Testing PDF")

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def runtrialbalancereports(request):

    display_data = processDataRunTrialBalance()
    return render(request, 'pages/runTrialBalanceReports.html', {"url": "/dashboard/reports/run-trial-balance", "display_data": display_data})


def processDataRunTrialBalance():
    data = []
    data.append({
        'name': "Account name goes here",
        'unadjusted_balance': 100,
        'entry': 0,
        'adjusted_balance': 90
    })
    data.append({
        'name': "Account name goes here 2",
        'unadjusted_balance': 100,
        'entry': 0,
        'adjusted_balance': 90
    })
    return data


def generate_run_trial_balance(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Add the text "testing pdf" to the PDF
    p.drawString(100, 750, "Testing PDF")

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def generalledgerreports(request):
    return render(request, 'pages/generalLedgerReports.html', {"url": "/dashboard/reports/general-ledger"})


def generate_general_ledger_reports(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Add the text "testing pdf" to the PDF
    p.drawString(100, 750, "Testing PDF")

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def inventoryreports(request):
    try:
        user = User.objects.get(username=request.user)
        inventories = Inventory.objects.filter(user=user)
    except Exception as e:
        return redirect('/')

    display_data = processDataInventory(inventories)

    return render(request, 'pages/inventoryReports.html', {'display_data': display_data, "url": "/dashboard/reports/inventory-report"})


def processDataInventory(inventories):
    data = []

    for inventory in inventories:
        histories = InventoryHistory.objects.filter(inventory=inventory)

        for history in histories:
            data.append({
                'name': inventory.name,
                'product': inventory.product.name,
                'price_per_unit': inventory.price_per_unit,
                'stock': history.current_stock
            })

    return data


def generate_inventory_reports(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Add the text "testing pdf" to the PDF
    p.drawString(100, 750, "Testing PDF")

    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
