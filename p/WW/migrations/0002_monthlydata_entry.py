# Generated by Django 5.1.4 on 2025-01-22 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WW', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveSmallIntegerField()),
                ('total_income', models.FloatField(default=0.0)),
                ('total_expenses', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WW.user')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('emoji', models.CharField(blank=True, max_length=10)),
                ('frequency', models.CharField(choices=[('monthly', 'Monthly'), ('yearly', 'Yearly'), ('one-time', 'One-time')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WW.user')),
                ('monthly_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='WW.monthlydata')),
            ],
        ),
    ]
