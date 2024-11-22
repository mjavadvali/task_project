from rest_framework import serializers
from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "category", 
                  "description", "available", 
                  "price", "image"]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']