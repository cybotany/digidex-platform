from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from digidex.inventory.models import Digit


class DigitDetailsView(LoginRequiredMixin, DetailView):
    model = Digit
    template_name = 'inventory/digit-details-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        return get_object_or_404(queryset, uuid=uuid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = self.object

        # Access the related Journal Collection and the first 10 entries
        journal_entries = digit.journal_collection.entries.all()
        context['journal_entries'] = journal_entries[:10]

        last_image_entry = journal_entries.filter(image__isnull=False).order_by('-created_at').first()
        context['last_image'] = last_image_entry.image if last_image_entry else None

        return context
