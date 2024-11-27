from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartItems.as_view(), name='cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart-add'),
    path('add/<int:product_id>/<int:quantity>/', views.cart_add, name='cart-add-quantity'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart-remove'),
    path('clear/', views.cart_clear, name='cart-clear'),

]
