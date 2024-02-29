from django.views.generic import DetailView
from django.http import Http404
from digidex.inventory.models import MODEL_MAP

class DetailDigit(DetailView):
    context_object_name = 'digit'
    template_name = 'inventory/digit/detail-page.html'

    def get_object(self, queryset=None):
        digit_type = self.kwargs.get('type')
        uuid = self.kwargs.get('uuid')

        if not uuid or not digit_type:
            raise Http404("No UUID or digit type provided")

        model = MODEL_MAP.get(digit_type)
        if not model:
            raise Http404(f"Invalid digit type '{digit_type}'")

        obj = model.objects.filter(uuid=uuid).first()
        if obj:
            self.model = model
            return obj
        else:
            raise Http404("No matching object found")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = self.object
        user = self.request.user

        is_owner = user.is_authenticated and digit.ntag.user == user
        journal_entries = digit.get_journal_entries() if digit.is_public or is_owner else []
        
        context.update({
            'is_owner': is_owner,
            'journal_entries': journal_entries,
        })

        return context
