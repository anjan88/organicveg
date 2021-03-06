# Generated by Django 3.0.5 on 2020-04-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamvegan', '0024_auto_20200421_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(blank=True, choices=[('LARGE', 'LARGE'), ('SMALL', 'SMALL'), ('MEDIUM', 'MEDIUM'), ('EXTRA LARGE', 'EXTRA LARGE')], max_length=11),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
