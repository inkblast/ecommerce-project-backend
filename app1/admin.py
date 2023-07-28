

# Register your models here.
from django.contrib import admin
from .models import Shop_Order, Delivered, Order_status, Shipping_method, Order_line

class Shop_OrderAdmin(admin.ModelAdmin):
    list_display = ('codesKey', 'product_name', 'product_quentity', 'product_price', 'cust_name', 'cust_email', 'cust_address', 'cust_phone','date_created','order_status')

admin.site.register(Shop_Order, Shop_OrderAdmin)

class Shipping_MethodAdmin(admin.ModelAdmin):
    list_display = ('codesKey', 'product_name', 'product_quentity', 'product_price', 'cust_name', 'cust_email', 'cust_address', 'cust_phone','date_created','order_status')

admin.site.register(Delivered, Shipping_MethodAdmin)

class Order_statusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

admin.site.register(Order_status,Order_statusAdmin)

class Shipping_methodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

admin.site.register(Shipping_method,Shipping_methodAdmin)

class Order_lineAdmin(admin.ModelAdmin):
    list_display = ('id', 'customize_product_id','order_id','qty','price')

admin.site.register(Order_line,Order_lineAdmin)
