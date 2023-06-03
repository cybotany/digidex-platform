from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..forms import GrowthChamberForm


class GrowthChamberRegistrationView(LoginRequiredMixin, View):
    template_name = 'cea/growth_chamber_registration.html'

    def get(self, request):
        form = GrowthChamberForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = GrowthChamberForm(request.POST)
        if form.is_valid():
            growth_chamber = form.save(commit=False)
            growth_chamber.user = request.user
            growth_chamber.save()
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)
