# Generated by Django 4.2.5 on 2023-10-20 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_auto_20231020_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuserrelationship',
            name='account',
            field=models.ForeignKey(blank=True, db_column='account_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='report.account'),
        ),
    ]