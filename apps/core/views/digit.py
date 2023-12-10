from django.views.generic import DetailView
from django.shortcuts import redirect, render
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateJournalEntry(request.POST, request.FILES)

        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.digit = self.object  # Link the journal entry to the current Digit
            journal_entry.user = request.user  # Set the user
            journal_entry.save()
            return redirect(self.object.get_absolute_url())  # Redirect back to the Digit detail page

        # If the form is not valid, re-render the page with the form errors
        context = self.get_context_data(object=self.object)
        context['journal_entry_form'] = form
        return render(request, self.template_name, context)
