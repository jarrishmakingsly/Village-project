# Generated by Django 3.2 on 2021-05-04 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villageapp', '0002_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='Panchayath',
        ),
    ]
