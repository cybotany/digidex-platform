from django.db.models import Prefetch
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Pet
from digidex.journal.models import Entry

class DetailPet(DetailView):
    model = Pet
    template_name = 'inventory/pet/detail-page.html'

    def get_object(self, queryset=None):
        # Prefetch related objects to optimize database queries for journal entries
        queryset = queryset or self.get_queryset().prefetch_related(
            Prefetch('journal_entries', queryset=Entry.objects.order_by('-created_at'))
        )
        uuid = self.kwargs.get('uuid')
        if not uuid:
            raise Http404("No UUID provided")
        pet = get_object_or_404(queryset, uuid=uuid)

        # Permission check
        if not pet.is_public:
            user = self.request.user
            if not user.is_authenticated or pet.ntag.user != user:
                raise PermissionDenied("You do not have permission to view this pet.")

        return pet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.object
        user = self.request.user

        is_owner = user.is_authenticated and pet.ntag.user == user

        # Assuming Pet model has a relationship with journal entries similar to the Digit model
        journal_entries = pet.journal_entries.all() if pet.is_public or is_owner else []

        context.update({
            'journal_entries': journal_entries,
            'is_owner': is_owner
        })

        return context
