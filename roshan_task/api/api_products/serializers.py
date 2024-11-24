from rest_framework import serializers
from products.models import Product, Category


        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.title")
    class Meta:
        model = Product
        fields = ["title", "category", "description", "available", "price", "image"]