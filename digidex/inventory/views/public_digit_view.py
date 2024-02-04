from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from digidex.inventory.models import Digit


class PublicDigitView(DetailView):
    model = Digit
    template_name = 'inventory/public-digit-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        return get_object_or_404(queryset, uuid=uuid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = self.object
        context.update({
            'heading': digit.name,
            'paragraph': digit.description,
            'date': digit.created_at.strftime("%b %d, %Y"),
        })
        return context
