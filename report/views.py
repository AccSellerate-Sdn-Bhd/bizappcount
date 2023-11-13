from django.shortcuts import render, redirect
from user_onboard.models import User, Product
from inventory.models import Inventory, InventoryHistory
from django.http import JsonResponse, HttpResponse
import io
from django.http import FileResponse
from report.models import Journal, Ledger, AccountUserRelationship, Account
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
from urllib.parse import unquote
from io import BytesIO
from datetime import datetime


from .forms import FilterForm

# Create your views here.


def monthToNumber(month_name):
    month_dict = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    return month_dict.get(month_name, None)


def pandlreports(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    form = FilterForm()

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            start_date = str(form.cleaned_data['start_date'])
            end_date = str(form.cleaned_data['end_date'])

            date_format = "%Y-%m-%d"
            start = DateFunction.strptime(start_date, date_format)
            end = DateFunction.strptime(end_date, date_format)
            
            convertLedgerToAccounts(start, end, user)

    accounts = AccountUserRelationship.objects.filter(user=user.user_id)

    data = []
    total = 0

    if (len(accounts) > 0):
        types = []
        for useraccount in accounts:

            if useraccount.account.type in types:
                type_object = next(
                    (item for item in data if item["title"] == useraccount.account.type), None)
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

    return render(request, 'pages/pandlReports.html', {
        "url": "/dashboard/reports/profit-and-loss",
        "form": form,
        "data": data,
        "total": total
    })


def convertToLedger(request, url):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    url = unquote(url)

    journals = Journal.objects.filter(editable=1, user=user.user_id)
    currentime = DateFunction.now()

    balance = 0

    for journal in journals:
        balance = balance - \
            float(journal.credit_amount) if journal.debit_amount == None else balance + \
            float(journal.debit_amount)

        ledger = Ledger(
            account=journal.account,
            journal=journal,
            user=user,
            datetime=journal.datetime,
            name=journal.name,
            description=journal.description,
            debit_amount=journal.debit_amount,
            credit_amount=journal.credit_amount,
            balance=balance
        )

        useraccount = AccountUserRelationship.objects.filter(
            user=user.user_id, account=journal.account.account_id)
        if (len(useraccount) > 0):
            olduseraccount = useraccount.first()

            new_amount = float(olduseraccount.amount) - float(
                journal.credit_amount) if journal.debit_amount == None else float(olduseraccount.amount) + journal.debit_amount
            olduseraccount.amount = new_amount
            olduseraccount.save()
        else:
            newuseraccount = AccountUserRelationship(
                user=user,
                account=journal.account,
                amount=-
                float(
                    journal.credit_amount) if journal.debit_amount == None else journal.debit_amount
            )
            newuseraccount.save()

        journal.editable = 0
        journal.save()
        ledger.save()

    return redirect('/dashboard/reports/' + url)


def convertLedgerToAccounts(start_date, end_date, user):

    ledgers = Ledger.objects.filter(
        datetime__gte=start_date,
        datetime__lt=end_date
    )

    print(ledgers)
    resetAccounts(user)

    for ledger in ledgers:
        useraccount = AccountUserRelationship.objects.filter(
            user=user.user_id, account=ledger.account.account_id)
        if (len(useraccount) > 0):
            olduseraccount = useraccount.first()

            new_amount = float(olduseraccount.amount) - float(
                ledger.credit_amount) if ledger.debit_amount == None else float(olduseraccount.amount) + ledger.debit_amount
            olduseraccount.amount = new_amount
            olduseraccount.save()
        else:
            newuseraccount = AccountUserRelationship(
                user=user,
                account=ledger.account,
                amount=-
                float(
                    ledger.credit_amount) if ledger.debit_amount == None else ledger.debit_amount
            )
            newuseraccount.save()


def resetAccounts(user):
    useraccounts = AccountUserRelationship.objects.filter(user=user.user_id)

    for account in useraccounts:
        account.amount = 0
        account.save()


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


def getData(account_name, user):
    parent_acc = Account.objects.get(name=account_name)
    child_accounts = Account.objects.filter(parent_acc_id=parent_acc)
    total = 0

    data = []
    for acc in child_accounts:
        ledgers = Ledger.objects.filter(
            account_id=acc.account_id, user=user.user_id)
        data = data + list(ledgers)
        for ledger in ledgers:
            total = total + (float(ledger.credit_amount)
                             if ledger.credit_amount is not None else -float(ledger.debit_amount))

    aggregated_data = {}

    for ledger in data:
        name = ledger.name
        amount = float(
            ledger.credit_amount) if ledger.credit_amount is not None else -float(ledger.debit_amount)

        # Check if the name already exists in the aggregated data
        if name in aggregated_data:
            # If it does, add the amount to the existing total
            aggregated_data[name] += amount
        else:
            # If it doesn't, create a new entry
            aggregated_data[name] = amount

    # Convert the aggregated data back to a list of objects
    result = [{'name': name, 'amount': amount}
              for name, amount in aggregated_data.items()]

    newObject = {
        "title": account_name,
        "data": result,
        "total": total
    }

    return newObject


def getBalanceSheetData(user):
    accounts = AccountUserRelationship.objects.filter(user=user.user_id)
    data = []
    total = 0

    if (len(accounts) > 0):
        types = []
        for useraccount in accounts:
            acc_array = ["assets", "fixed assets", "liabilities", "equity"]
            if useraccount.account.type in acc_array:
                if useraccount.account.type in types:
                    type_object = next(
                        (item for item in data if item["title"] == useraccount.account.type), None)
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

    return data


def getAccount(data, title):
    found_object = None
    for obj in data:
        if obj["title"] == title:
            found_object = obj
            break

    if found_object is not None:
        total = 0
        for obj in found_object['data']:
            total = total + obj.amount
        return {
            "title": found_object['title'],
            "data": found_object['data'],
            "total": total
        }
    else:
        return {
            "title": title,
            "data": [],
            "total": 0
        }


def balancesheetreports(request):
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    form = FilterForm()

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            start_date = str(form.cleaned_data['start_date'])
            end_date = str(form.cleaned_data['end_date'])

            date_format = "%Y-%m-%d"
            start = DateFunction.strptime(start_date, date_format)
            end = DateFunction.strptime(end_date, date_format)

            convertLedgerToAccounts(start, end, user)

    displaydata = getBalanceSheetData(user)

    print("\n\n\n\n\n")
    assets = getAccount(displaydata, "assets")
    liabilities = getAccount(displaydata, "liabilities")
    fixed_assets = getAccount(displaydata, "fixed assets")
    equity = getAccount(displaydata, "equity")

    compareAssetLiabilities = len(assets['data']) > len(liabilities['data'])
    compareFixedAssetsEquity = len(fixed_assets['data']) > len(equity['data'])

    return render(request, 'pages/balancesheetReports.html', {
        "url": "/dashboard/reports/balance-sheet",
        "form": form,
        "assets": assets,
        "liabilities": liabilities,
        "compareAssetLiabilities": compareAssetLiabilities,
        "totalAssets": float(assets['total']) + float(fixed_assets['total']),
        "fixed_assets": fixed_assets,
        "equity": equity,
        "compareFixedAssetsEquity": compareFixedAssetsEquity,
        "totalLiabilities": float(equity['total']) + float(liabilities['total'])
    })


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
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    form = FilterForm()

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            start_date = str(form.cleaned_data['start_date'])
            end_date = str(form.cleaned_data['end_date'])

            date_format = "%Y-%m-%d"
            start = DateFunction.strptime(start_date, date_format)
            end = DateFunction.strptime(end_date, date_format)

            convertLedgerToAccounts(start, end, user)

    displaydata = getCashFlowData(user)

    print("\n\n\n\n\n")
    revenues = getAccount(displaydata, "revenue")
    expenses = getAccount(displaydata, "expenses")

    net_cash_flow = 0
    ending_balance = 0

    for revenue in revenues['data']:
        net_cash_flow = net_cash_flow + float(revenue.amount)
        ending_balance = ending_balance + float(revenue.amount)

    for expense in expenses['data']:
        net_cash_flow = net_cash_flow - float(expense.amount)
        ending_balance = ending_balance - float(expense.amount)

    return render(request, 'pages/cashflowReports.html', {
        "url": "/dashboard/reports/cash-flow",
        "form": form,
        'revenues': revenues,
        "expenses": expenses,
        "net_cash_flow": net_cash_flow,
        "ending_balance": ending_balance
    })


def getCashFlowData(user):
    accounts = AccountUserRelationship.objects.filter(user=user.user_id)
    data = []
    total = 0

    if (len(accounts) > 0):
        types = []
        for useraccount in accounts:
            acc_array = ["revenue", "expenses"]
            if useraccount.account.type in acc_array:
                if useraccount.account.type in types:
                    type_object = next(
                        (item for item in data if item["title"] == useraccount.account.type), None)
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
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    ledgers = Ledger.objects.filter(user=user.user_id)

    form = FilterForm()

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            start_date = str(form.cleaned_data['start_date'])
            end_date = str(form.cleaned_data['end_date'])

            date_format = "%Y-%m-%d"
            start = DateFunction.strptime(start_date, date_format)
            end = DateFunction.strptime(end_date, date_format)

            ledgers = Ledger.objects.filter(
                datetime__gte=start,
                datetime__lt=end
            )

    return render(request, 'pages/runTrialBalanceReports.html', {
        "url": "/dashboard/reports/run-trial-balance",
        "display_data": ledgers,
        "form": form
    })


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
    try:
        user = User.objects.get(username=request.user)
    except Exception as e:
        return redirect('/')

    ledgers = Ledger.objects.filter(user=user.user_id)

    form = FilterForm()

    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            start_date = str(form.cleaned_data['start_date'])
            end_date = str(form.cleaned_data['end_date'])

            date_format = "%Y-%m-%d"
            start = DateFunction.strptime(start_date, date_format)
            end = DateFunction.strptime(end_date, date_format)

            ledgers = Ledger.objects.filter(
                datetime__gte=start,
                datetime__lt=end
            )

    return render(request, 'pages/generalLedgerReports.html', {
        "url": "/dashboard/reports/general-ledger",
        "ledgers": ledgers,
        "form": form
    })


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

        data.append({
            'name': inventory.name,
            'product': inventory.product.name,
            'price_per_unit': inventory.price_per_unit,
            'stock': inventory.amount
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
