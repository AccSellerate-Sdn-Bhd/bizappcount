from django.db import models
from user_onboard.models import User

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    amount  = models.FloatField()
    interval  = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    
    class Meta:
        db_table = 'bill'
# Create your models here.
