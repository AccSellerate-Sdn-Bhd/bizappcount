# Generated by Django 4.2.5 on 2023-09-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_onboard', '0013_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='date_joined',
            field=models.DateField(),
        ),
    ]
