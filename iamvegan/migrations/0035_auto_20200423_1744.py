# Generated by Django 3.0.5 on 2020-04-23 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0034_auto_20200423_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_product',
            name='image',
            field=models.ImageField(default='', upload_to='featuredproduct'),
        ),
    ]
