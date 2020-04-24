from django.contrib import admin
from iamvegan.models import Featured_Product,Product,Order,Billingdetail,Cart,Picture

# Register your models here.


class Featured_ProductsAdmin(admin.ModelAdmin):

     list_display = ('id','name','price','discounted_price','category','label','image')
     search_fields = ('name','category','price')
     list_editable = ('name','price', 'discounted_price', 'category', 'label', 'image')


class ProductsAdmin(admin.ModelAdmin):

     list_display = ('id','name','price','discounted_price','category','label','image')
     search_fields = ('name','category','price')
     list_editable = ('name','category','price','discounted_price','label','image')


class OrderAdmin(admin.ModelAdmin):

     list_display = ('orderid','orderdate')
     search_fields = ('orderid','orderdate')


class BillingdetailAdmin(admin.ModelAdmin):

     list_display = ('firstname', 'lastname','emailaddress','phonenumber','streetaddress','city','state','country','pincode','totalprice')
     search_fields = ('firstname', 'lastname','emailaddress','phonenumber')

class CartAdmin(admin.ModelAdmin):
    pass

class PictureAdmin(admin.ModelAdmin):
    list_display = ('choices_image','images')



admin.site.register(Featured_Product, Featured_ProductsAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Billingdetail, BillingdetailAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Picture, PictureAdmin)