# Generated by Django 4.2.5 on 2023-10-11 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='expense',
            table='expenses',
        ),
        migrations.AlterModelTable(
            name='expenseattachment',
            table='expense_attachment',
        ),
        migrations.AlterModelTable(
            name='expenselineitem',
            table='expense_line_item',
        ),
    ]
