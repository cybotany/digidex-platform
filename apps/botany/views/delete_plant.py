from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from apps.botany.models import Plant


class DeletePlantView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """
    View for rendering the page used for deleting registered plants.
    """
    template_name = 'botany/delete_plant.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.delete_plant()
        self.add_success_message()
        return self.redirect_to_home()

    def get_object(self):
        return get_object_or_404(Plant, pk=self.kwargs['pk'])

    def test_func(self):
        return self.request.user == self.get_object().owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant'] = self.get_object()
        return context

    def delete_plant(self):
        self.get_object().delete()

    def add_success_message(self):
        message = 'Your plant was successfully deleted!'
        messages.success(self.request, message)

    def redirect_to_home(self):
        return redirect('botany:home')