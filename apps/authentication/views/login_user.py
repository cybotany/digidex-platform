from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/login_user.html'
