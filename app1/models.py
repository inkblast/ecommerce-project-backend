from django.db import models
from datetime import date

# Create your models here.
class Shop_Order(models.Model):
    codesKey = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=100)
    product_quentity = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    cust_name = models.CharField(max_length=100)
    cust_email = models.CharField(max_length=100)
    cust_address = models.CharField(max_length=100)
    cust_phone = models.CharField(max_length=10)
    date_created = models.DateField(default=date.today)
    order_status = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class Delivered(models.Model):
    codesKey = models.IntegerField(primary_key = True)
    product_name = models.CharField(max_length=100)
    product_quentity = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    cust_name = models.CharField(max_length=100)
    cust_email = models.CharField(max_length=100)
    cust_address = models.CharField(max_length=100)
    cust_phone = models.CharField(max_length=10)
    date_created =  models.CharField(max_length=10)
    order_status = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
    
class Order_status(models.Model):
    id = models.IntegerField(primary_key = True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.id

class Shipping_method(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.id

class Order_line(models.Model):
    id = models.AutoField(primary_key = True)
    customize_product_id = models.IntegerField()
    order_id = models.IntegerField()
    qty = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.id
