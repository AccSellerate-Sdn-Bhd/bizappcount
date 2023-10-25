# Generated by Django 4.2.5 on 2023-10-22 11:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expense_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField()),
                ('payee', models.CharField(max_length=45)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('recurring', models.BooleanField(default=False)),
                ('recurring_date', models.DateTimeField(blank=True, null=True)),
                ('recurring_amount', models.FloatField(blank=True, null=True)),
                ('payment_type', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'expenses',
            },
        ),
        migrations.CreateModel(
            name='ExpenseAttachment',
            fields=[
                ('attachment_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('file', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'expense_attachment',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='receipts/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('expense_id', models.ForeignKey(db_column='expense_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipts', to='expenses.expense')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseLineItem',
            fields=[
                ('expense_line_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('unit_discount', models.FloatField()),
                ('total_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('expense_id', models.ForeignKey(db_column='expense_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='line_items', to='expenses.expense')),
            ],
            options={
                'db_table': 'expense_line_item',
            },
        ),
    ]