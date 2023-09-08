from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.nfc.forms import NFCTagForm
from apps.nfc.models import NFCTag


class RegisterTagView(LoginRequiredMixin, CreateView):
    model = NFCTag
    form_class = NFCTagForm
    template_name = 'nfc/register_tag.html'
    success_url = reverse_lazy('botany:home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)