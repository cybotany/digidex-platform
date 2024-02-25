from django.db.models import Prefetch
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Digit
from digidex.journal.models import Entry


class DigitDetailsView(DetailView):
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
        if not digit.is_public:
            user = self.request.user
            if not user.is_authenticated or digit.ntag.user != user:
                raise PermissionDenied("You do not have permission to view this digit.")

        return digit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = self.object
        user = self.request.user

        is_owner = user.is_authenticated and digit.ntag.user == user

        journal_collection = digit.journal_collection
        journal_entries = journal_collection.get_all_entries() if digit.is_public or is_owner else []

        context.update({
            'journal_entries': journal_entries,
            'is_owner': is_owner
        })

        return context