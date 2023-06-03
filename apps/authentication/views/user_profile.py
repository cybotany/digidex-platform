from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class UserProfile(LoginRequiredMixin, View):
    template_name = 'authentication/profile.html'

    def get(self, request, *args, **kwargs):
        context = {'user': request.user}
        return render(request, self.template_name, context)
