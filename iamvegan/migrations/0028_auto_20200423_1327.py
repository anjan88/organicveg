# Generated by Django 3.0.5 on 2020-04-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0027_auto_20200423_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]