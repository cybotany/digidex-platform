from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..models import Plant, Trial


class DashboardView(LoginRequiredMixin, View):
    template_name = 'cybotany/dashboard.html'

    def get(self, request, *args, **kwargs):
        # Get the current user
        user = request.user

        # Get the plants and trials associated with the current user
        plants = Plant.objects.filter(user=user)
        trials = Trial.objects.filter(user=user)

        context = {
            'plants': plants,
            'trials': trials,
        }

        return render(request, self.template_name, context)
