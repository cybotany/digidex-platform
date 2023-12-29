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
        context['journal_entry_form'] = CreateJournalEntry(digit=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateJournalEntry(request.POST, request.FILES, digit=self.object, user=request.user)

        if form.is_valid():
            form.save()
            return redirect(self.object.get_absolute_url())  # Redirect back to the Digit detail page

        # If the form is not valid, re-render the page with the form errors
        context = self.get_context_data(object=self.object)
        context['journal_entry_form'] = form
        return render(request, self.template_name, context)
