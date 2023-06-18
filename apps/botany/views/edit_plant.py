from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from ..models import Plant

class PlantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Plant
    fields = ['name', 'description', 'image']
    template_name = 'botany/plant_edit.html'
    success_url = reverse_lazy('botany:home')

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.owner

    def form_valid(self, form):
        messages.success(self.request, 'Your plant was successfully updated!')
        return super().form_valid(form)
