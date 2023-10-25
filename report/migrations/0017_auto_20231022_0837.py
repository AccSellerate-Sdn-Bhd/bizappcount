from django.db import migrations
from report.models import Account, TransactionAction

def seed_data(apps, schema_editor):
    #Main accounts
    expenses = Account.objects.create(
        name="Expenses",
        type="expenses",
    )

    #Child accounts
    bizapp_software = Account.objects.create(
        name="BizApp Software",
        type="expenses",
        parent_acc=expenses
    )

    bizapp_count_software = Account.objects.create(
        name="BizApp Count Software",
        type="expenses",
        parent_acc=expenses
    )

    email_software = Account.objects.create(
        name="Email Software",
        type="expenses",
        parent_acc=expenses
    )

    website_hosting = Account.objects.create(
        name="Website Hosting",
        type="expenses",
        parent_acc=expenses
    )

    domain_renewals = Account.objects.create(
        name="Domain Renewals",
        type="expenses",
        parent_acc=expenses
    )

    software_name = Account.objects.create(
        name="Software Name",
        type="expenses",
        parent_acc=expenses
    )

    account_payable = Account.objects.filter(name="Account Payable").first()

    #Expense Actions
    #1
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - BizApp Software",
        payment="Credit",
        model="ExpenseLineItem",
        datafield="total_price",
        account=bizapp_software,
        operation=1
    )
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - BizApp Software",
        payment="Credit",
        model="Product",
        datafield="cost",
        account=account_payable,
        operation=0
    )
    
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - BizApp Count Software",
        payment="Credit",
        model="ExpenseLineItem",
        datafield="total_price",
        account=bizapp_count_software,
        operation=1
    )
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - BizApp Count Software",
        payment="Credit",
        model="Product",
        datafield="cost",
        account=account_payable,
        operation=0
    )

    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - Email Software",
        payment="Credit",
        model="ExpenseLineItem",
        datafield="total_price",
        account=email_software,
        operation=1
    )
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - Email Software",
        payment="Credit",
        model="Product",
        datafield="cost",
        account=account_payable,
        operation=0
    )

    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - Website Hosting",
        payment="Credit",
        model="ExpenseLineItem",
        datafield="total_price",
        account=website_hosting,
        operation=1
    )
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - Website Hosting",
        payment="Credit",
        model="Product",
        datafield="cost",
        account=account_payable,
        operation=0
    )

    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - Domain Renewals",
        payment="Credit",
        model="ExpenseLineItem",
        datafield="total_price",
        account=domain_renewals,
        operation=1
    )
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software - Domain Renewals",
        payment="Credit",
        model="Product",
        datafield="cost",
        account=account_payable,
        operation=0
    )

    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software Expenses - Software Name",
        payment="Credit",
        model="ExpenseLineItem",
        datafield="total_price",
        account=software_name,
        operation=1
    )
    TransactionAction.objects.create(
        name="Software Expenses",
        expense_title="Software Expenses - Software Name",
        payment="Credit",
        model="Product",
        datafield="cost",
        account=account_payable,
        operation=0
    )


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_auto_20231020_2048'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]