from django.db import models
from computed_property import ComputedFloatField, ComputedCharField

# Create your models here.
CATEGORY_CHOICES = (('Fruits', 'Fruits'),
                    ('Juices', 'Juices'),
                    ('Veggies', 'Veggies'),
                    ('Dried', 'Dried')
                    )

LABEL_CHOICES = (('Farm Fresh', 'Farm Fresh'),
                 ('Organic', 'Organic'),
                 ('Extract', 'Extract')
                 )

SIZE = (('LARGE', 'LARGE'),
        ('SMALL', 'SMALL'),
        ('MEDIUM', 'MEDIUM'),
        ('EXTRA LARGE', 'EXTRA LARGE')
        )



class Featured_Product(models.Model):

    def __str__(self):
        return id==id

    name = models.CharField(blank=True, max_length=200)
    price = models.FloatField(blank=True)
    discounted_price = models.FloatField(blank=True)
    category = models.CharField(max_length=7, blank=True, choices=CATEGORY_CHOICES)
    label = models.CharField(max_length=10, blank=True, choices=LABEL_CHOICES)
    image = models.ImageField(default='', upload_to='featured')
    quantity = models.IntegerField(default=1)
    afterdiscount = ComputedFloatField(blank=True, compute_from='calculation1')
    totalprice = ComputedFloatField(blank=True, compute_from='calculation2')
    taxes = models.FloatField(default=2)
    stock = models.PositiveIntegerField(default=0)

    @property
    def calculation1(self):
        return self.price - (self.discounted_price / 100) * self.price

    @property
    def calculation2(self):
        return self.price * self.quantity + self.taxes


class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    label = models.CharField(max_length=10, choices=LABEL_CHOICES)
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField(default=1)
    afterdiscount = ComputedFloatField(default=0, compute_from='calculation1')
    totalprice = ComputedFloatField(default=0, compute_from='calculation2')
    taxes = models.FloatField()

    @property
    def calculation1(self):
        return self.price - (self.discounted_price / 100) * self.price

    @property
    def calculation2(self):
        return self.price * self.quantity + self.taxes


class Billingdetail(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailaddress = models.EmailField()
    phonenumber = models.IntegerField()
    streetaddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    taxes = models.FloatField()
    afterdiscount = ComputedFloatField(default=0, compute_from='calculation1')
    totalprice = ComputedFloatField(default=0, compute_from='calculation2')
    username = ComputedCharField(default="null", max_length=100, compute_from='calculation3')

    @property
    def calculation3(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def calculation1(self):
        return self.price - (self.discounted_price / 100) * self.price

    @property
    def calculation2(self):
        return self.afterdiscount * self.quantity + self.taxes


class Order(models.Model):
    orderid = models.IntegerField(unique=True)
    orderdate = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)


class Cart(models.Model):
    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=11,blank=True,choices=SIZE)



class Picture(models.Model):

    IMAGECHOICES = (('BACKGROUND_IMAGES', 'BACKGROUND_IMAGES'),
                    ('ABOUT_US_IMAGES', 'ABOUT_US_IMAGES'),
                    ('CATEGORY_IMAGES', 'CATEGORY_IMAGES'),
                    ('PARTNER_IMAGES', 'PARTNER_IMAGES')
                    )

    choices_image = models.CharField(max_length=20,choices=IMAGECHOICES)
    images = models.ImageField(blank=True, upload_to='')


