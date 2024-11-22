from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveAPIView, 
    ListAPIView, 
    RetrieveUpdateDestroyAPIView,
) 
from .permissions import IsAdminOrReadOnly
from products.models import Product, Category
from rest_framework.permissions import IsAdminUser


class ProductListCreate(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

        return Response(
            ProductSerializer(self.get_queryset(), many=True).data,
            status=status.HTTP_201_CREATED
        )
    

class ProductRetrieve(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]



class CategoryListCreate(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class CategoryRetrieve(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class ProductsByCategoryView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Product.objects.filter(category_id=category_id)