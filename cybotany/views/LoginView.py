from django.contrib.auth import login
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy

class LoginView(DjangoLoginView):
    template_name = 'cybotany/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')
