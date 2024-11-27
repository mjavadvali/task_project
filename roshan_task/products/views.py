from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.generics import (
    ListCreateAPIView, 
    ListAPIView, 
    RetrieveUpdateDestroyAPIView,
) 
from .permissions import IsAdminOrReadOnly
from products.models import Product, Category
from rest_framework.permissions import IsAdminUser
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

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

    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()
        hit_count = HitCount.objects.get_for_object(product)
        HitCountMixin.hit_count(request, hit_count) 
        return super().retrieve(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     product.pk
    #     return super().delete(request, *args, **kwargs)


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
        category_id = self.kwargs['pk']
        return Product.objects.filter(category_id=category_id)