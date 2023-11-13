# Generated by Django 4.2.5 on 2023-10-19 17:35

from django.db import migrations
from report.models import Account, TransactionAction

# account_id = models.AutoField(primary_key=True, max_length=255)
# name = models.CharField(max_length=45)
# type = models.CharField(max_length=45, null=True, blank=True)
# parent_acc = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_column='parent_acc_id')


def seed_data(apps, schema_editor):
    #Main accounts
    revenue = Account.objects.create(
        name="Revenue",
        type="revenue",
    )
    liabilities = Account.objects.create(
        name="Liabilities",
        type="liabilities",
    )
    assets = Account.objects.create(
        name="Assets",
        type="assets",
    )
    equity = Account.objects.create(
        name="Equity",
        type="equity",
    )
    cost_of_sales = Account.objects.create(
        name="Cost of Sales",
        type="cost of sales",
    )

    #Child accounts
    cash_account = Account.objects.create(
        name="Cash Account",
        type="assets",
        parent_acc=assets
    )
    cash_account_bizapp = Account.objects.create(
        name="Cash Account (BizApp)",
        type="assets",
        parent_acc=assets
    )
    cost_of_sales_inventory = Account.objects.create(
        name="Cost of Sales (Inventory)",
        type="cost of sales",
        parent_acc=cost_of_sales
    )
    cost_of_sales_dropshipping = Account.objects.create(
        name="Cost of Sales (Dropshipping)",
        type="cost of sales",
        parent_acc=cost_of_sales
    )
    sales_revenue = Account.objects.create(
        name="Sales Revenue",
        type="revenue",
        parent_acc=revenue
    )
    inventory = Account.objects.create(
        name="Inventory",
        type="assets",
        parent_acc=assets
    )
    account_receivables = Account.objects.create(
        name="Account Receivables",
        type="assets",
        parent_acc=assets
    )
    account_payable = Account.objects.create(
        name="Account Payable",
        type="assets",
        parent_acc=liabilities
    )

    #Sales Actions
    #1
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Cash",
        model="SalesLineItems",
        datafield="total_price",
        account=cash_account_bizapp,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Cash",
        model="Product",
        account=cost_of_sales_inventory,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Cash",
        model="SalesLineItems",
        datafield="total_price",
        account=sales_revenue,
        operation=0
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Cash",
        model="Product",
        account=inventory,
        operation=0
    )

    #2
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Credit",
        model="SalesLineItems",
        datafield="total_price",
        account=account_receivables,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Credit",
        model="Product",
        account=cost_of_sales_inventory,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Credit",
        model="SalesLineItems",
        datafield="total_price",
        account=sales_revenue,
        operation=0
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp Sales- with Inventory",
        payment="Credit",
        model="Product",
        account=inventory,
        operation=0
    )

    #3
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Cash",
        model="SalesLineItems",
        datafield="total_price",
        account=cash_account_bizapp,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Cash",
        model="Product",
        account=cost_of_sales_dropshipping,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Cash",
        model="SalesLineItems",
        datafield="total_price",
        account=sales_revenue,
        operation=0
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Cash",
        model="Product",
        account=inventory,
        operation=0
    )

    #4
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Credit",
        model="SalesLineItems",
        datafield="total_price",
        account=account_receivables,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Credit",
        model="Product",
        account=cost_of_sales_dropshipping,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Credit",
        model="SalesLineItems",
        datafield="total_price",
        account=sales_revenue,
        operation=0
    )
    TransactionAction.objects.create(
        name="Sales Revenue (BizApp)",
        sales_title="BizApp - without Inventory",
        payment="Credit",
        model="SalesLineItems",
        datafield="total_price",
        account=account_payable,
        operation=0
    )

    #5
    TransactionAction.objects.create(
        name="Sales Revenue (POS BizApp)",
        sales_title="BizApp POS -with Inventory",
        payment="Cash",
        model="SalesLineItems",
        datafield="total_price",
        account=cash_account_bizapp,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (POS BizApp)",
        sales_title="BizApp POS -with Inventory",
        payment="Cash",
        model="Product",
        account=cost_of_sales_inventory,
        operation=1
    )
    TransactionAction.objects.create(
        name="Sales Revenue (POS BizApp)",
        sales_title="BizApp POS -with Inventory",
        payment="Cash",
        model="SalesLineItems",
        datafield="total_price",
        account=sales_revenue,
        operation=0
    )
    TransactionAction.objects.create(
        name="Sales Revenue (POS BizApp)",
        sales_title="BizApp POS -with Inventory",
        payment="Cash",
        model="Product",
        account=inventory,
        operation=0
    )

class Migration(migrations.Migration):

    dependencies = [
        ('report', '003_alter_transactionaction_account'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
