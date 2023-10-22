from django.db import models
from user_onboard.models import Address, Business, User ,Product
import uuid
class Expense(models.Model):
    expense_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id')  # Assuming User model from Django's built-in auth
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    payee = models.CharField(max_length=45)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    recurring = models.BooleanField(default=False)  # Using BooleanField for TINYINT
    recurring_date = models.DateTimeField(blank=True, null=True)
    recurring_amount = models.FloatField(blank=True, null=True)
    payment_type = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'expenses'


class ExpenseLineItem(models.Model):
    expense_line_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='product_id')
    unit_discount = models.FloatField()
    total_price = models.FloatField()
    quantity = models.IntegerField()
    expense_id = models.ForeignKey(Expense, on_delete=models.DO_NOTHING, related_name='line_items',db_column='expense_id')
    class Meta:
        db_table = 'expense_line_item'

class ExpenseAttachment(models.Model):
    attachment_id = models.CharField(primary_key=True, max_length=255)
    file = models.CharField(max_length=255)
    expense_id = models.ForeignKey(Expense, on_delete=models.DO_NOTHING ,db_column='expense_id', related_name='attachments')
    class Meta:
        db_table = 'expense_attachment'


class Receipt(models.Model):
    file = models.FileField(upload_to='receipts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    expense_id = models.ForeignKey(Expense, on_delete=models.DO_NOTHING ,db_column='expense_id', related_name='receipts')