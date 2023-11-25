from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import login


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login_user.html'
