# Generated by Django 4.2.5 on 2023-09-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_onboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
