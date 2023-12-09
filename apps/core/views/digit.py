from django.views.generic import DetailView
from apps.core.models import Digit
from apps.core.forms import CreateJournalEntry


class DigitView(DetailView):
    model = Digit
    template_name = 'digit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_entries'] = self.object.journal_entries.all()
        context['journal_entry_form'] = CreateJournalEntry()
        return context
