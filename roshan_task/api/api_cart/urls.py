from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartItems.as_view(), name='api-cart'),
    path('add/<int:product_id>/', views.cart_add, name='api-cart-add'),
    path('remove/<int:product_id>/', views.cart_remove, name='api-cart-remove'),
    path('clear/', views.cart_clear, name='api-cart-clear'),

]
