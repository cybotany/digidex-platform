from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class AccountDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'cybotany/dashboard.html'
