from django.conf import settings
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import Grouping

class DetailGrouping(DetailView):
    model = Grouping
    template_name = 'inventory/grouping/detail-page.html'

    def get_object(self, queryset=None):
        user_slug = self.kwargs.get('user_slug')
        group_slug = self.kwargs.get('group_slug')

        if not user_slug or not group_slug:
            raise Http404("No sufficient identifiers provided")

        user = get_object_or_404(settings.AUTH_USER_MODEL, slug=user_slug)

        # Adjust the query to match your model's structure. Assuming Grouping model has a 'name' or 'slug' field
        grouping = get_object_or_404(Grouping, slug=group_slug, user=user)  # Adjust 'name' to your field

        # Permission check (adjust according to your Grouping model's fields and privacy logic)
        if not grouping.is_public:
            if not self.request.user.is_authenticated or grouping.user != self.request.user:
                raise PermissionDenied("You do not have permission to view this grouping.")

        return grouping

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouping = self.object
        user = self.request.user

        is_owner = user.is_authenticated and grouping.user == user

        # Assuming Grouping model relates to some entries you want to display
        # Adjust the context as needed based on your actual data models
        entries = grouping.entries.all() if grouping.is_public or is_owner else []

        context.update({
            'entries': entries,
            'is_owner': is_owner
        })

        return context
