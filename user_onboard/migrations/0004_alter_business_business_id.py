# Generated by Django 4.2.5 on 2023-09-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_onboard', '0003_alter_address_address_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
