# Generated by Django 3.0.5 on 2020-04-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0035_auto_20200423_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_product',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
