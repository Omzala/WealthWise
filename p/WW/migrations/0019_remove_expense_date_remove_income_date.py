# Generated by Django 5.1.4 on 2025-02-24 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WW', '0018_remove_expense_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
        migrations.RemoveField(
            model_name='income',
            name='date',
        ),
    ]
