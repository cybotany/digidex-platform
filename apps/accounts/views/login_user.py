from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.contrib.auth import login


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login_user.html'

    def form_valid(self, form):
        super().form_valid(form)
        
        refresh = RefreshToken.for_user(self.request.user)
        access_token = str(refresh.access_token)
        
        # Return JWT token in the response
        return JsonResponse({
            'access_token': access_token,
            'refresh_token': str(refresh)
        })
