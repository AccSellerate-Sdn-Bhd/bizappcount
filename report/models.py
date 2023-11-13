from django.db import models
from user_onboard.models import User
from sales.models import Sales
from expenses.models import Expense

class Account(models.Model):
    account_id = models.AutoField(primary_key=True, max_length=255)
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45, null=True, blank=True)
    parent_acc = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_column='parent_acc_id')

    class Meta:
        db_table = 'account'

class AccountUserRelationship(models.Model):
    relationship_id = models.AutoField(primary_key=True, max_length=255)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, db_column='user_id')
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.DO_NOTHING, db_column='account_id')
    amount = models.FloatField(null=True)
    class Meta:
        db_table = 'user_account'


class TransactionAction(models.Model):
    action_id = models.AutoField(primary_key=True, max_length=255)
    sales_title = models.CharField(max_length=255, null=True, blank=True)
    expense_title = models.CharField(max_length=255, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column='account_id', null=True)
    
    # to determine which data to use to update
    model = models.CharField(max_length=255, null=True, blank=True)
    datafield = models.CharField(max_length=255, null=True, blank=True)

    name = models.CharField(max_length=255)
    payment = models.CharField(max_length=255, null=True, blank=True)
    operation = models.BooleanField()  # Assuming TINYINT is used as boolean (0 or 1)

    class Meta:
        db_table = 'transaction_action'


class Journal(models.Model):
    journal_id = models.AutoField(primary_key=True, max_length=255)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column='account_id')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, db_column='user_id')
    datetime = models.DateTimeField()
    name = models.CharField(max_length=45)
    debit_amount = models.FloatField(null=True)
    credit_amount = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    editable = models.BooleanField(default=True)
    sales_id = models.ForeignKey(Sales, on_delete=models.DO_NOTHING, db_column='sales_id', null=True)
    expense_id = models.ForeignKey(Expense, on_delete=models.DO_NOTHING, db_column='expense_id', null=True)
    type = models.CharField(max_length=25, null=True ,default=None)

    class Meta:
        db_table = 'journal'


class Ledger(models.Model):
    ledger_id = models.AutoField(primary_key=True, max_length=255)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column='account_id')
    journal = models.ForeignKey(Journal, on_delete=models.DO_NOTHING, db_column='journal_id')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, db_column='user_id')
    datetime = models.DateTimeField()
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255, null=True, blank=True)
    debit_amount = models.FloatField(null=True)
    credit_amount = models.FloatField(null=True)
    balance = models.FloatField()

    class Meta:
        db_table = 'ledger'