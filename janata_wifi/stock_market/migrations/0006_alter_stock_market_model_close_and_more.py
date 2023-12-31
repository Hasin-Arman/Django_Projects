# Generated by Django 4.2.3 on 2023-09-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_market', '0005_rename_open_value_stock_market_model_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_market_model',
            name='close',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stock_market_model',
            name='date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stock_market_model',
            name='high',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stock_market_model',
            name='low',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stock_market_model',
            name='open',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='stock_market_model',
            name='volume',
            field=models.CharField(max_length=30),
        ),
    ]
