# Generated by Django 4.2.3 on 2023-08-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressmodel',
            name='street_address',
            field=models.CharField(default='ctg', max_length=100),
        ),
    ]
