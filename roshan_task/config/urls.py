from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('cart/', include('cart.urls')),

    path('api/', include('api.api_products.urls')),
    path('api/cart/', include('api.api_cart.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),

    path('api/login', LoginView.as_view(), name='login')
    

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


