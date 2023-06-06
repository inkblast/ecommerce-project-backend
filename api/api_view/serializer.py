from rest_framework import serializers
from .models import product

class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    
    
    def create(self, data):
        return product.objects.create(**data)
    
    def update(self, instance, data):
        instance.category_id = data.get('category_id', instance.category_id)
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.quantity = data.get('quantity', instance.quantity)
        
        instance.save()
        return instance
        