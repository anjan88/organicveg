# Generated by Django 3.0.5 on 2020-04-21 23:22

import computed_property.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0017_auto_20200421_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured_product',
            name='featured_product',
        ),
        migrations.AddField(
            model_name='billingdetail',
            name='username',
            field=computed_property.fields.ComputedCharField(compute_from='calculation3', default='null', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='afterdiscount',
            field=computed_property.fields.ComputedFloatField(compute_from='calculation1', default=0, editable=False),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('Juices', 'Juices'), ('Veggies', 'Veggies'), ('Dried', 'Dried')], default='Veggies', max_length=7),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='discounted_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='image',
            field=models.ImageField(default='image/images/product-1.jpg', upload_to='image/images'),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='label',
            field=models.CharField(choices=[('Farm Fresh', 'Farm Fresh'), ('Organic', 'Organic'), ('Extract', 'Extract')], default='SMALL', max_length=10),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='name',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='price',
            field=models.FloatField(default=1000),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='taxes',
            field=models.FloatField(default=2),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='totalprice',
            field=computed_property.fields.ComputedFloatField(compute_from='calculation2', default=0, editable=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderid',
            field=models.IntegerField(unique=True),
        ),
    ]
