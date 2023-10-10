# Generated by Django 4.2.5 on 2023-09-27 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_onboard', '0014_alter_staff_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('collection', models.CharField(max_length=255)),
                ('SKU', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('cost', models.FloatField()),
                ('forex', models.IntegerField()),
                ('retail_selling_price', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]