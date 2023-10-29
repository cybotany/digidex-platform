from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.cea.models import GrowthChamber, Greenhouse, TissueCultureChamber


class CEAHomepageView(LoginRequiredMixin, View):
    template_name = 'cea/homepage.html'

    def get(self, request, *args, **kwargs):
        cea_chambers = {
            'Growth Chambers': GrowthChamber.objects.filter(user=request.user),
            'Greenhouses': Greenhouse.objects.filter(user=request.user),
            'Tissue Culture Chambers': TissueCultureChamber.objects.filter(user=request.user),
        }
        return render(request, self.template_name, {'cea_chambers': cea_chambers})
