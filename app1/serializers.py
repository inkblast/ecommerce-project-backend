
from rest_framework import serializers
from app1.models import Shop_Order
from app1.models import Delivered
from app1.models import Order_status
from app1.models import Shipping_method
from app1.models import Order_line

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_Order
        fields = ['codesKey', 'product_name', 'product_quentity', 'product_price', 'cust_name', 'cust_email', 'cust_address', 'cust_phone','date_created','order_status']  

class DeliveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivered
        fields = ['codesKey', 'product_name', 'product_quentity', 'product_price', 'cust_name', 'cust_email', 'cust_address', 'cust_phone','date_created','order_status']


class Order_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_status
        fields = ['id', 'status']

class Shipping_methodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_method
        fields = ['id' , 'name' , 'price']

class Order_lineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_line
        fields = ['id', 'customize_product_id', 'order_id', 'qty', 'price']