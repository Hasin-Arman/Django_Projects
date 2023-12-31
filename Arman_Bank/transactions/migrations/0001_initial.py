# Generated by Django 4.2.3 on 2023-09-27 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('balance_after_transaction', models.IntegerField()),
                ('transaction_type', models.IntegerField(choices=[(1, 'deposit'), (2, 'withdraw'), (3, 'loan'), (4, 'loan_paid')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('loan_approved', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.userbankaccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
