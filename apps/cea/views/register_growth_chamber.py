from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from apps.cea.forms import GrowthChamberRegistrationForm


class RegisterGrowthChamber(LoginRequiredMixin, View):
    template_name = 'cea/new_growth_chamber.html'

    def get(self, request):
        form = GrowthChamberRegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = GrowthChamberRegistrationForm(request.POST)
        if form.is_valid():
            growth_chamber = form.save(commit=False)
            growth_chamber.user = request.user
            growth_chamber.save()
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)
