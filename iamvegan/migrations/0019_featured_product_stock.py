# Generated by Django 3.0.5 on 2020-04-22 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0018_auto_20200421_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured_product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
