from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from ..forms import SignupForm


class SignupUser(View):
    template_name = 'authentication/signup.html'

    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)
