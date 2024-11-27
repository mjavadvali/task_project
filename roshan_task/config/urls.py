from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import LoginView, LogoutView


from dj_rest_auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from . import register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('cart/', include('cart.urls')),

    path('api/', include('api.api_products.urls')),
    path('api/cart/', include('api.api_cart.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),

    path('api/auth/token/', LoginView.as_view(), name='login'),
    path('api/auth/token/logout/', LogoutView.as_view(), name='logout'),

    path('auth/', register_views.CustomLoginView.as_view(), name='custom-login'),
    path('auth/logout/', register_views.CustomLogoutView.as_view(), name='custom-logout'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


