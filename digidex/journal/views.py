from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from digidex.journal.forms import JournalEntry
from .models import Digit, NFC

class DigitJournalView(View):
    def post(self, request, serial_number):
        nfc = get_object_or_404(NFC, serial_number=serial_number)
        digit = get_object_or_404(Digit, nfc_link=nfc)

        form = JournalEntry(request.POST, request.FILES)
        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.digit = digit
            journal_entry.save()
            return HttpResponseRedirect(request.path_info)

        # Handle invalid form
        # ...

    # Optionally, add a get method if needed