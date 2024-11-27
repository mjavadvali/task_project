from rest_framework import serializers
from products.serializers import ProductSerializer

class CartSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()
