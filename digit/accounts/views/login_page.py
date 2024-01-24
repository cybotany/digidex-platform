from django.contrib.auth.views import LoginView
from digit.accounts.forms import LoginForm

class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'main/login-page.html'
