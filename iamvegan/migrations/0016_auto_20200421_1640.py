# Generated by Django 3.0.5 on 2020-04-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0015_auto_20200421_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured_product',
            name='size',
            field=models.CharField(choices=[('LARGE', 'LARGE'), ('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('EXTRA LARGE', 'EXTRA LARGE')], default=4, max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='billingdetail',
            name='phonenumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='featured_product',
            name='image',
            field=models.ImageField(upload_to='image/images/'),
        ),
    ]
