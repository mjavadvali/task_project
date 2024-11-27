from dj_rest_auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'custom_login.html' 
    redirect_authenticated_user = True  
    success_url = reverse_lazy('products_list')  
    def get(self, request):
        return render(request, self.template_name)

    def get_success_url(self):
        return self.success_url or super().get_success_url()