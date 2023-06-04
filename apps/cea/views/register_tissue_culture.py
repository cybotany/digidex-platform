from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..forms import TissueCultureRegistrationForm


class RegisterTissueCultureChamber(LoginRequiredMixin, View):
    template_name = 'cea/new_tissue_culture_chamber.html'

    def get(self, request):
        form = TissueCultureRegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TissueCultureRegistrationForm(request.POST)
        if form.is_valid():
            tissue_culture_chamber = form.save(commit=False)
            tissue_culture_chamber.user = request.user
            tissue_culture_chamber.save()
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)
