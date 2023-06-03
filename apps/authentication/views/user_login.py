from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/login.html'
