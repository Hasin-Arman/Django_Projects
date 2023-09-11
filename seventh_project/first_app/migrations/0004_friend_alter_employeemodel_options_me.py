# Generated by Django 4.2.3 on 2023-08-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_employeemodel_managermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=20)),
                ('attendence', models.BooleanField()),
                ('hw', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='employeemodel',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('first_app.friend',),
        ),
    ]
