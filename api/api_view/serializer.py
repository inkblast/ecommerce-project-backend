from rest_framework import serializers
from .models import product,product_category,promotion
class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    sku = serializers.IntegerField()
    
    
    def create(self, data):
        return product.objects.create(**data)
    
    def update(self, instance, data):
        instance.category_id = data.get('category_id', instance.category_id)
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.quantity = data.get('quantity', instance.quantity)
        instance.price = data.get('price', instance.price)
        instance.sku = data.get('sku', instance.sku)
        
        instance.save()
        return instance
        
class Products_CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, data):
        return product_category.objects.create(**data)
    
    def update(self, instance, data):
        instance.category_id = data.get('category_id', instance.category_id)
        instance.name = data.get('name', instance.name)
        
        instance.save()
        return instance
    
class PromotionSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=400)
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M" )
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    def create(self, data):
        return promotion.objects.create(**data)
    
    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.start_date = data.get('start_date', instance.start_date)
        instance.end_date = data.get('end_date', instance.end_date)
        
        instance.save()
        return instance