# Generated by Django 3.1.5 on 2023-03-18 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balanceSheet', models.FileField(upload_to='')),
                ('date_added', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenditureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenditure_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FixedAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=100)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='otherExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spent_on', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('date_added', models.DateField()),
                ('remarks', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_added', models.DateField()),
                ('remarks', models.CharField(blank=True, max_length=100)),
                ('receipt', models.FileField(blank=True, upload_to='iemodule/income_receipts')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomeSource', to='income_expenditure.incomesource')),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date_added', models.DateField()),
                ('remarks', models.CharField(max_length=100)),
                ('expenditure_receipt', models.FileField(upload_to='iemodule/expenditure_receipts')),
                ('spent_on', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expenditureType', to='income_expenditure.expendituretype')),
            ],
        ),
    ]
