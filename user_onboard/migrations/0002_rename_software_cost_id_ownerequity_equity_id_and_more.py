# Generated by Django 4.2.5 on 2023-11-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_onboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownerequity',
            old_name='software_cost_id',
            new_name='equity_id',
        ),
        migrations.AddField(
            model_name='bank',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bank',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loan',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='ownerequity',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ownerequity',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='softwarecost',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='softwarecost',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='staff',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]