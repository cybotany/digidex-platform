from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

class LogoutUser(LogoutView):
    next_page = reverse_lazy('main:landing')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged off.")
        return super().dispatch(request, *args, **kwargs)
