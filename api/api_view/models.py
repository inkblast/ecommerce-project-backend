from django.db import models

# Create your models here.
class product(models.Model):
    category_id = models.IntegerField()
    quantity = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField(null=True)
    sku = models.IntegerField(null=True)
    
    def __str__(self):
        return self.product_id
class product_category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def _str_(self):
        return self.category_id
    