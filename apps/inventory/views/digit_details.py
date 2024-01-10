from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit
from apps.journal.forms import CreateJournalEntry


class DigitDetailsView(LoginRequiredMixin, DetailView):
    model = Digit
    template_name = 'inventory/digit_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Initialize the form with the current digit and user
        if self.request.method == 'GET':
            context['journal_form'] = CreateJournalEntry(initial={
                'digit': self.object,
                'user': self.request.user
            })

        return context