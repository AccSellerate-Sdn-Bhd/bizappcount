# Generated by Django 4.2.5 on 2023-10-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_remove_transactionaction_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionaction',
            name='datafield',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transactionaction',
            name='payment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]