from django.db.models import Prefetch
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Plant
from digidex.journal.models import Entry


class PlantDetails(DetailView):
    model = Plant
    template_name = 'inventory/plants/plant-details-page.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset().prefetch_related(
            Prefetch('journal_collection__entries', queryset=Entry.objects.order_by('-created_at'))
        )
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No uuid provided")
        plant = get_object_or_404(queryset, uuid=uuid)

        # Permission check
        if not plant.is_public:
            user = self.request.user
            if not user.is_authenticated or plant.ntag.user != user:
                raise PermissionDenied("You do not have permission to view this Plant.")

        return plant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plant = self.object
        user = self.request.user

        is_owner = user.is_authenticated and plant.ntag.user == user

        journal_collection = plant.journal_collection
        journal_entries = journal_collection.get_all_entries() if plant.is_public or is_owner else []

        context.update({
            'journal_entries': journal_entries,
            'is_owner': is_owner
        })

        return context