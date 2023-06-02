from django.shortcuts import render, redirect
from ..forms import UserForm
from django.contrib.auth import login
from django.views import View


class AccountSignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})
