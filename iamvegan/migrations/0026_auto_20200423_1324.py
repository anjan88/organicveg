# Generated by Django 3.0.5 on 2020-04-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0025_auto_20200422_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_product',
            name='image',
            field=models.ImageField(default='image/images/product-1.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]