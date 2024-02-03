from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.inventory.models import Digit


class DigitStorageView(LoginRequiredMixin, ListView):
    model = Digit
    context_object_name = 'digits'
    template_name = 'inventory/digit-storage-page.html'

    def get_queryset(self):
        """ Overriding to get Digits for the current user """
        return Digit.objects.filter(nfc_link__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['subtitle'] = 'Storage'
        context['heading'] = 'Storage Box n'
        context['paragraph'] = 'Details about Storage Box n'

        return context
