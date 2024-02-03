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
        journal_collection = digit.journal_collection
        context.update({
            'subtitle': 'Overview',
            'heading': digit.name,
            'paragraph': digit.description,
            'date': digit.created_at.strftime("%b %d, %Y"),
            'summarized_content': journal_collection.get_summarized_content(),
            'image_carousel_data': journal_collection.get_image_carousel_data()
        })

        return context