"""organicveg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iamvegan import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Iamvegan'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('blog/', views.blogpage, name='blogpage'),
    path('blogsingle/', views.blogsinglepage, name='blogsinglepage'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('<int:id>/', views.product, name='product'),
    path('<int:id>/', views.featrued, name='featrued'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('fruits/', views.fruits, name='fruits'),
    path('juices/', views.juices, name='juices'),
    path('dries/', views.dries, name='dries'),

]

urlpatterns += [
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
