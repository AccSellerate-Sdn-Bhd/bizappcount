from django.db import models
from user_onboard.models import User, Product

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    amount  = models.FloatField()
    unit  = models.CharField(max_length=255)
    price_per_unit = models.FloatField()
    
    class Meta:
        db_table = 'inventory'

class InventoryHistory(models.Model):
    inventory_history_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True)
    current_stock = models.FloatField(default=0)
    increase = models.BooleanField()
    amount = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        db_table = 'inventory_history'