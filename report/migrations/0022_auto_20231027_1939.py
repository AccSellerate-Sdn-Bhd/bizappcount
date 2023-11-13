# Generated by Django 4.2.5 on 2023-10-27 19:39

from django.db import migrations
from report.models import Account

class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        fixed_assets = Account.objects.create(
            name="Fixed Assets",
            type="fixed assets",
        )

    dependencies = [
        ('report', '0021_auto_20231027_1720'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]