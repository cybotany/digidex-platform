from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from apps.botany.models import Plant


class UpdatePlantView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Plant
    fields = ['name', 'description',]
    template_name = 'botany/update_plant.html'
    success_url = reverse_lazy('botany:home')

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.owner

    def form_valid(self, form):
        messages.success(self.request, 'Your plant was successfully updated!')
        return super().form_valid(form)
