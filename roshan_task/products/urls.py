from django.urls import path
from . import views
 
urlpatterns = [
    path('products', views.ProductList.as_view(), name='products_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('categories', views.CategoryList.as_view(), name='categories_list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('categories/<int:pk>/products', views.CategoryProductsList.as_view(), name='category_products'),

]
