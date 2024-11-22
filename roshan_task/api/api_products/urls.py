from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ProductListCreate.as_view(), name='api-product-list-create'),
    path('products/<int:pk>', views.ProductRetrieve.as_view(), name='api-product-retrieve'),
    path('categories', views.CategoryListCreate.as_view(), name='api-categories-list-create'),
    path('categories/<int:pk>', views.CategoryRetrieve.as_view(), name='api-category-retrieve'),
    path('api/categories/<int:pk>', views.ProductsByCategoryView.as_view(), name='products-by-category'),
]
