from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..forms import GreenhouseRegistrationForm


class RegisterGreenhouse(LoginRequiredMixin, View):
    template_name = 'cea/new_greenhouse.html'

    def get(self, request):
        form = GreenhouseRegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = GreenhouseRegistrationForm(request.POST)
        if form.is_valid():
            greenhouse = form.save(commit=False)
            greenhouse.user = request.user
            greenhouse.save()
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)
