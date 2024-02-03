from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from digidex.accounts.forms import SignupForm
from digidex.accounts.models import User

class SignupUserView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup-page.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:confirm-email')

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})