# Generated by Django 4.2.5 on 2023-09-27 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_onboard', '0018_rename_loans_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareCost',
            fields=[
                ('software_cost_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('software_billing_info', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('billing_duration', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'software_cost',
            },
        ),
    ]
