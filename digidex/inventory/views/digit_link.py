from django.views import View
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, render
from digidex.inventory.models import Digit
from digidex.link.models import NFC
from digidex.journal.models import Collection
from digidex.inventory.forms import DigitForm


class DigitLinkView(LoginRequiredMixin, SingleObjectMixin, View):
    model = NFC

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        serial_number = self.kwargs.get('serial_number')
        if not serial_number:
            raise Http404("No serial number provided")
        return get_object_or_404(queryset, serial_number=serial_number)

    def get(self, request, *args, **kwargs):
        nfc = self.get_object()
        nfc.increment_counter()
        if not nfc.active:
            return self.handle_digit_creation(request, nfc)
        self.handle_digit_details(request, nfc)

    def handle_digit_creation(self, request, nfc):
        form = DigitForm(request.POST or None)
        if form.is_valid():
            digit = Digit.create_digit(form.cleaned_data, nfc, request.user)
            return self.handle_digit_details(request, digit)
        return render(request, 'inventory/digit-creation-page.html', {'form': form, 'errors': form.errors})

    def handle_digit_details(self, request, nfc):
        if not nfc.check_access(request.user):
            return HttpResponseForbidden("Unauthorized access")

        digit = get_object_or_404(Digit, nfc_link=nfc)
        journal_collection = Collection.objects.filter(digit=digit).first()
        return render(request, 'inventory/digit-details-page.html', {'digit': digit, 'journal_collection': journal_collection})
