from django.urls import path
from . import views
 
urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductRetrieve.as_view(), name='product_detail'),
    path('categories/', views.CategoryListCreate.as_view(), name='categories_list'),
    path('categories/<int:pk>/', views.CategoryRetrieve.as_view(), name='category_detail'),
    path('categories/<int:pk>/products/', views.ProductsByCategoryView.as_view(), name='category_products'),

]
