# Generated by Django 3.0.5 on 2020-04-21 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0013_auto_20200421_0155'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Billingdetails',
            new_name='Billingdetail',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
