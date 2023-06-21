from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from apps.botany.models import Plant


class DeletePlantView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'botany/delete_plant.html'

    def get_object(self):
        return get_object_or_404(Plant, pk=self.kwargs['pk'])

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant'] = self.get_object()
        return context

    def post(self, request, *args, **kwargs):
        plant = self.get_object()
        plant.delete()
        messages.success(self.request, 'Your plant was successfully deleted!')
        return redirect('botany:home')
