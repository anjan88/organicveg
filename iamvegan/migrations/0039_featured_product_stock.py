# Generated by Django 3.0.5 on 2020-04-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0038_remove_featured_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured_product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
