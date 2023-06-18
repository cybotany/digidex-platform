from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from ..models import Plant


class DeletePlant(LoginRequiredMixin, DeleteView):
    model = Plant
    template_name = 'botany/plant_delete_confirmation.html'
    success_url = reverse_lazy('botany:home')

    def delete(self, request, *args, **kwargs):
        plant = self.get_object()
        if self.request.user == plant.owner:
            messages.success(self.request, 'Plant successfully deleted.')
            return super(DeletePlant, self).delete(request, *args, **kwargs)
        else:
            messages.error(self.request, 'You do not have permission to delete this plant.')
            return reverse_lazy('botany:home')
