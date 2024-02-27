from django.db.models import Prefetch
from django.views.generic import DetailView
from django.http import Http404
from digidex.inventory.models import MODEL_MAP
from digidex.journal.models import Entry

class DetailDigit(DetailView):
    def get_object(self, queryset=None):
        digit_type = self.kwargs.get('type')
        uuid = self.kwargs.get('uuid')

        if not uuid or not digit_type:
            raise Http404("No UUID or digit type provided")

        model = MODEL_MAP.get(digit_type)
        if not model:
            raise Http404(f"Invalid digit type '{digit_type}'")

        obj_queryset = model.objects.prefetch_related(
            Prefetch('journal_entries', queryset=Entry.objects.order_by('-created_at'))
        )
        obj = obj_queryset.filter(uuid=uuid).first()
        if obj:
            self.model = model
            self.template_name = f'inventory/{model.__name__.lower()}/detail-page.html'
            return obj
        else:
            raise Http404("No matching object found")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = self.object
        user = self.request.user

        is_owner = user.is_authenticated and digit.ntag.user == user
        journal_entries = digit.journal_entries.all() if digit.is_public or is_owner else []

        context.update({
            'journal_entries': journal_entries,
            'is_owner': is_owner
        })

        return context
