from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login_user.html'
