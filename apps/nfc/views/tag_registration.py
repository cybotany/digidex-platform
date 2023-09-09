from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.nfc.models import NFCTag
from apps.nfc.forms import NFCTagForm


class RegisterTagView(LoginRequiredMixin, CreateView):
    model = NFCTag
    form_class = NFCTagForm
    template_name = 'nfc/register_tag.html'
    success_url = reverse_lazy('botany:home')

    def dispatch(self, request, *args, **kwargs):
        self.nfc_serial_number = kwargs.get('pk')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nfc_serial_number'] = self.nfc_serial_number
        return context

    def form_valid(self, form):
        nfc = get_object_or_404(NFCTag, tag_id=self.nfc_serial_number)
        if not nfc.active:
            nfc.active = True
            nfc.save()
            form.instance.created_by = self.request.user
            return super().form_valid(form)
        else:
            form.add_error('tag_id', 'This NFC tag is already registered.')
            return self.form_invalid(form)