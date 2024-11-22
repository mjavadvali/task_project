from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartItems.as_view(), name='api-cart'),
]
