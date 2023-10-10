# Generated by Django 4.2.5 on 2023-10-02 07:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_customer_alter_sales_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleslineitems',
            name='sales_line_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]