from rest_framework import serializers
from .models import product

class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    
    def create(self, data):
        return product.objects.create(**data)
    
    def update(self, instance, data):
        instance.category_id = data.get('category_id', instance.category_id)
        instance.product_name = data.get('product_name', instance.product_name)
        instance.product_details = data.get('product_details', instance.product_details)
        
        instance.save()
        return instance
        