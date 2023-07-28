from django.shortcuts import render

# Create your views here.
from .serializers import MenuSerializer
from .serializers import DeliveredSerializer
from .serializers import Order_statusSerializer
from .serializers import Shipping_methodSerializer
from .serializers import Order_lineSerializer
from rest_framework import viewsets      
from .models import Shop_Order    
from .models import Delivered    
from .models import Order_status
from .models import Shipping_method
from .models import Order_line        

class Shop_OrderView(viewsets.ModelViewSet):  
    serializer_class = MenuSerializer   
    queryset = Shop_Order.objects.all()  

class DeliveredView(viewsets.ModelViewSet):  
    serializer_class = DeliveredSerializer   
    queryset = Delivered.objects.all()  

class Order_status(viewsets.ModelViewSet):
    serializer_class =  Order_statusSerializer
    queryset =  Order_status.objects.all()

class Shipping_method(viewsets.ModelViewSet):
    serializer_class = Shipping_methodSerializer
    queryset = Shipping_method.objects.all()

class Order_line(viewsets.ModelViewSet):
    serializer_class = Order_lineSerializer
    queryset = Order_line.objects.all()


