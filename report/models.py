from django.db import models
from user_onboard.models import Address, Business, User ,Product

class Account(models.Model):
    account_id = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id')
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45, null=True, blank=True)
    amount = models.FloatField()
    parent_acc = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, db_column='parent_acc_id')

    class Meta:
        db_table = 'account'


class TransactionAction(models.Model):
    action_id = models.CharField(primary_key=True, max_length=255)
    sales_title = models.CharField(max_length=255, null=True, blank=True)
    expense_title = models.CharField(max_length=255, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column='account_id')
    name = models.CharField(max_length=255)
    payment = models.CharField(max_length=255, null=True, blank=True)
    operation = models.BooleanField()  # Assuming TINYINT is used as boolean (0 or 1)

    class Meta:
        db_table = 'transaction_action'


class Journal(models.Model):
    journal_id = models.CharField(primary_key=True, max_length=255)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column='account_id')
    datetime = models.DateTimeField()
    name = models.CharField(max_length=45)
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'journal'


class Ledger(models.Model):
    ledger_id = models.CharField(primary_key=True, max_length=255)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_column='account_id')
    journal = models.ForeignKey(Journal, on_delete=models.DO_NOTHING, db_column='journal_id')
    datetime = models.DateTimeField()
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255, null=True, blank=True)
    debit_amount = models.FloatField()
    credit_amount = models.FloatField()
    balance = models.FloatField()

    class Meta:
        db_table = 'ledger'