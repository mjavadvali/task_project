from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/auth/token/', LoginView.as_view(), name='login'),
    path('api/auth/token/logout/', LogoutView.as_view(), name='logout'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


