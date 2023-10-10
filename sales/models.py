from django.db import models
from user_onboard.models import Address, Business, User ,Product
import uuid
class Customer(models.Model):
    customer_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    handphone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    delivery_address = models.TextField(null=True, blank=True)
    tax_information = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True) # Using URLField for web links
    facebook = models.URLField(max_length=255, null=True, blank=True)
    tiktok = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name  # return the name field as the string representation

    class Meta:
        db_table = 'customer'


class Sales(models.Model):
    sales_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id')
    customer_id =  models.ForeignKey(Customer, on_delete=models.DO_NOTHING, db_column='customer_id')
    title = models.CharField(max_length=255)
    bizapp_transaction_no = models.CharField(max_length=255)
    date = models.DateTimeField()
    document_number = models.CharField(max_length=255, null=True, blank=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=45, null=True, blank=True)
    recurring = models.BooleanField(null=False,default=False)
    recurring_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'sales'


class SalesLineItems(models.Model):
    sales_line_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='product_id')
    quantity = models.IntegerField()
    unit_discount = models.FloatField()
    total_price = models.FloatField()
    sales_id = models.ForeignKey(Sales, on_delete=models.DO_NOTHING,null=True, db_column='sales_id', related_name='line_items')

    class Meta:
        db_table = 'sales_line_items'


class SalesFooter(models.Model):
    sales_footer_id = models.CharField(primary_key=True, max_length=255)
    terms_and_condition = models.TextField()
    payment_terms = models.TextField(null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    sales_id = models.ForeignKey(Sales, on_delete=models.DO_NOTHING, null=True,db_column='sales_id')

    class Meta:
        db_table = 'sales_footer'


class ShippingInformation(models.Model):
    shipping_no = models.CharField(primary_key=True, max_length=255)
    tracking_no = models.CharField(max_length=255)
    weight = models.FloatField()
    pricing = models.FloatField()
    sales_id = models.ForeignKey(Sales, on_delete=models.DO_NOTHING,null=True, db_column='sales_id')

    class Meta:
        db_table = 'shipping_information'


