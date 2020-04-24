from django.shortcuts import render, redirect
from .models import Featured_Product, Order, Product, Billingdetail, Cart, Picture


# Create your views here.

def homepage(request):
    product_object = Featured_Product.objects.all()
    pic = Picture.objects.all()
    return render(request, "Iamvegan/index.html", {'product_object': product_object,'pic':pic})


def aboutpage(request):
    return render(request, "Iamvegan/about.html")


def blogpage(request):
    return render(request, "Iamvegan/blog.html")


def blogsinglepage(request):  # completed
    product_object1 = Featured_Product.objects.filter(category='Veggies').count()
    product_object2 = Featured_Product.objects.filter(category='Fruits').count()
    product_object3 = Featured_Product.objects.filter(category='Juices').count()
    product_object4 = Featured_Product.objects.filter(category='Dried').count()
    return render(request, "Iamvegan/blog-single.html",
                  {'product_object1': product_object1, 'product_object2': product_object2,
                   'product_object3': product_object3, 'product_object4': product_object4})


def cart(request):
    product_object = Product.objects.all()
    return render(request, "Iamvegan/cart.html", {'product_object': product_object})


def checkout(request):
    return render(request, "Iamvegan/checkout.html")


def contact(request):
    return render(request, "Iamvegan/contact.html")


def featrued(request, id):
    product_object1 = Featured_Product.objects.get(Featured_Product_id = id)
    return render(request, "Iamvegan/Featured_product_single.html", {'product_object1': product_object1})


def product(request, id):
    product_object2 = Product.objects.get(pk=id)
    return render(request, "Iamvegan/product_product_single.html", {'product_object2': product_object2})


def shop(request):
    product_object3 = Product.objects.all()
    return render(request, "Iamvegan/shop.html", {'product_object3': product_object3})


def wishlist(request):
    return render(request, "Iamvegan/wishlist.html")


def vegetables(request):
    vegetable = Product.objects.filter(category='Veggies')
    return render(request, "Iamvegan/vegetables.html",{'vegetable':vegetable})


def fruits(request):
    fruit = Product.objects.filter(category='Fruits')
    return render(request, "Iamvegan/fruits.html", {'fruit': fruit})


def dries(request):
    dried = Product.objects.filter(category='Dried')
    return render(request, "Iamvegan/dries.html", {'dried': dried})


def juices(request):
    juice = Product.objects.filter(category='Juices')
    return render(request, "Iamvegan/juices.html", {'juice': juice})


