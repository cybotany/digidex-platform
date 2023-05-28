from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import GrowthChamber


class AccountDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'cybotany/dashboard.html'
    
    def get(self, request):
        # Get user's growth chambers and plants
        growth_chambers = GrowthChamber.objects.filter(user=request.user)

        return render(request, self.template_name, {'growth_chambers': growth_chambers})