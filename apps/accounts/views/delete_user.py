from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib import messages


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your user profile has been successfully deleted.')
        return super(DeleteUserView, self).delete(request, *args, **kwargs)
