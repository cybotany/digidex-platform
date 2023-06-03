from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class UserLogin(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
