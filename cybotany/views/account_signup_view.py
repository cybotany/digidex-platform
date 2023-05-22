from django.shortcuts import render, redirect
from ..forms import NewUserForm
from django.contrib.auth import login
from django.views import View


class AccountSignupView(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, 'cybotany/signup.html', {'form': form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'cybotany/signup.html', {'form': form})
