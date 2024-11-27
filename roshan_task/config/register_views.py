
from dj_rest_auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('products_list')

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Welcome to the Custom HTML Page!",
            "user": request.user,
        }
        return render(request, "registration/custom_login.html", context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user = authenticate(request, username=request.POST["username"],
                                password=request.POST["password"])
            if user:
                login(request, user)
                next_url = self.request.GET.get('next', self.success_url)
                return redirect(next_url)
        return render(request, 'registration/login_failed.html')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('custom-login')  # Redirect after logout

    def post(self, request, *args, **kwargs):
        """Log out the user and redirect."""
        logout(request)  # Log out the user
        return redirect(self.next_page)  # Redirect to login page or other location

    def get(self, request, *args, **kwargs):
        """Handle logout via GET (optional)."""
        return self.post(request, *args, **kwargs)