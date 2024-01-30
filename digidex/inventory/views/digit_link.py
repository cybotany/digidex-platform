from django.shortcuts import get_object_or_404, render
from digidex.inventory.models import Digit
from digidex.link.views import BaseNFCLinkedView
from digidex.journal.models import Collection
from digidex.inventory.forms import DigitForm


class DigitLinkView(BaseNFCLinkedView):
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
        digit = get_object_or_404(Digit, nfc_link=nfc)
        journal_collection = Collection.objects.filter(digit=digit).first()
        return render(request, 'inventory/digit-details-page.html', {'digit': digit, 'journal_collection': journal_collection})
