from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class FindCEAView(LoginRequiredMixin, View):
    template_name = 'cea/find_cea.html'

    def get(self, request):
        return render(request, self.template_name)
