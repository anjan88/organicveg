# Generated by Django 3.0.5 on 2020-04-21 00:59

import computed_property.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0005_auto_20200420_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='afterdiscount',
            field=computed_property.fields.ComputedFloatField(compute_from='calculation', default=0, editable=False),
        ),
    ]
