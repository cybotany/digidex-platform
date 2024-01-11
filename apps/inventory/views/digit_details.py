from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.inventory.models import Digit
from apps.journal.forms import CreateJournalEntry
from apps.journal.models import Entry


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

        journal_entries = Entry.objects.filter(digit=self.object)
        context['journal_entries'] = journal_entries

        today = datetime.now().date()

        last_watering_entry = journal_entries.filter(watered=True).order_by('-created_at').first()
        context['last_watering_date'] = last_watering_entry.created_at if last_watering_entry else None
        context['days_since_last_watering'] = (today - last_watering_entry.created_at.date()).days if last_watering_entry else None

        last_fertilizing_entry = journal_entries.filter(fertilized=True).order_by('-created_at').first()
        context['last_fertilizing_date'] = last_fertilizing_entry.created_at if last_fertilizing_entry else None
        context['days_since_last_fertilizing'] = (today - last_fertilizing_entry.created_at.date()).days if last_fertilizing_entry else None
        
        last_cleaning_entry = journal_entries.filter(cleaned=True).order_by('-created_at').first()
        context['last_cleaning_date'] = last_cleaning_entry.created_at if last_cleaning_entry else None
        context['days_since_last_cleaning'] = (today - last_cleaning_entry.created_at.date()).days if last_cleaning_entry else None

        last_image_entry = journal_entries.filter(image__isnull=False).order_by('-created_at').first()
        context['last_image'] = last_image_entry.image if last_image_entry else None

        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateJournalEntry(request.POST, request.FILES)

        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.digit = self.object
            journal_entry.user = request.user
            journal_entry.save()

            return redirect(reverse('inventory:details', kwargs={'pk': self.object.pk}))

        context = self.get_context_data()
        context['journal_form'] = form
        return self.render_to_response(context)
