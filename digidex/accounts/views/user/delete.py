from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout


class DeleteUser(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()

        messages.success(request, 'Your account has been successfully deleted.')
        logout(request)
        return redirect('main:landing')
