from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from digidex.journal.models import Entry


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'journal/entry-details-page.html'
    context_object_name = 'entry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        entry = context.get('entry')

        context['subtitle'] = 'Journal Entry'
        context['heading'] = f'Entry {entry.entry_number}'
        context['date'] = entry.created_at.strftime('%B %d, %Y')
        context['paragraph'] = ''
        return context
