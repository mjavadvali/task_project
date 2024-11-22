from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>', views.cart_add, name='cart-add'),
    path('remove/<int:product_id>', views.cart_remove, name='cart-remove'),
    path('clear', views.cart_clear, name='cart-clear'),
    path('', views.cart_summary, name='cart-summary')
]
