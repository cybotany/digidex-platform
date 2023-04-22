from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View


class AccountSignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'cybotany/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'cybotany/signup.html', {'form': form})
