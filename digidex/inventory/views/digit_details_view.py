from django.db.models import Prefetch
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Digit
from digidex.journal.models import Entry


class DigitDetailsView(LoginRequiredMixin, DetailView):
    model = Digit
    template_name = 'inventory/digit-details-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset().prefetch_related(
            Prefetch('journal_collection__entries', queryset=Entry.objects.order_by('-created_at'))
        )
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        digit = get_object_or_404(queryset, uuid=uuid)

        # Permission check
        user = self.request.user
        if digit.nfc_link.user != user:
            raise PermissionDenied("You do not have permission to view this digit.")

        return digit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        digit = self.object
        journal_collection = digit.journal_collection
        summarized_content = journal_collection.get_summarized_content()
        image_carousel_data = journal_collection.get_image_carousel_data()
        
        context.update({
            'subtitle': 'Overview',
            'heading': digit.name,
            'paragraph': digit.description,
            'date': digit.created_at.strftime("%b %d, %Y"),
            'summarized_content': summarized_content,
            'image_carousel_data': image_carousel_data
        })

        return context