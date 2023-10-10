from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=1, default='')
    category = models.CharField(max_length=255)
    password = models.CharField(max_length=128, default='')

    class Meta:
        db_table = 'user'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.IntegerField()
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    GPS_location = models.CharField(max_length=45, null=True, blank=True)
    office_tel_no = models.CharField(max_length=45)

    class Meta:
        db_table = 'address'


class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    registration_no = models.IntegerField()
    website_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'business'


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    account_no = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    type = models.IntegerField()
    bizapp = models.BooleanField()

    class Meta:
        db_table = 'bank'


class Office(models.Model):
    office_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    rent = models.BooleanField()
    electric = models.IntegerField()
    water = models.IntegerField()
    internet = models.IntegerField()
    rental = models.IntegerField()
    rental_deposit = models.IntegerField()

    class Meta:
        db_table = 'office'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    ic_passport = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    date_joined = models.DateField()
    position = models.CharField(max_length=255)
    salary = models.FloatField()
    epf = models.FloatField()

    class Meta:
        db_table = 'staff'


class Product(models.Model):  # Inventory
    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    collection = models.CharField(max_length=255)
    SKU = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    cost = models.FloatField()
    forex = models.IntegerField()
    retail_selling_price = models.FloatField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    creditor = models.CharField(max_length=255)
    creditor_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    creditor_phone_no = models.CharField(max_length=255)
    
    amount = models.FloatField()
    amount_payable = models.FloatField()
    interest = models.FloatField()
    installment_amount = models.FloatField()
    not_defined = models.BooleanField()
    recurring = models.BooleanField()
    active = models.BooleanField()

    class Meta:
        db_table = 'loan'

class SoftwareCost(models.Model):
    software_cost_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    software_billing_info = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    billing_duration = models.CharField(max_length=255)
    amount = models.FloatField()
    active = models.BooleanField()

    class Meta:
        db_table = 'software_cost'

class OwnerEquity(models.Model):
    software_cost_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    ic_passport = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    bumiputera = models.BooleanField()
    percentage_ownership = models.FloatField()
    paid_up_capital = models.FloatField()

    class Meta:
        db_table = 'owner_equity'