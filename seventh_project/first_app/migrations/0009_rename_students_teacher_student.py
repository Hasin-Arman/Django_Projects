# Generated by Django 4.2.3 on 2023-08-17 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_alter_teacher_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='students',
            new_name='student',
        ),
    ]
