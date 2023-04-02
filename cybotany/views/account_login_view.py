from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class AccountLoginView(LoginView):
    template_name = 'cybotany/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')
