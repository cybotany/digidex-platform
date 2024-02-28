from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from digidex.inventory.models import Grouping

class DetailGrouping(DetailView):
    model = Grouping
    template_name = 'inventory/grouping/detail-page.html'

    def get_object(self, queryset=None):
        user_slug = self.kwargs.get('user_slug')
        group_slug = self.kwargs.get('group_slug')

        if user_slug and not group_slug:
            return redirect('inventory:detail-profile', user_slug=user_slug)
        if not user_slug or not group_slug:
            raise Http404("No sufficient identifiers provided")

        user = get_object_or_404(get_user_model(), slug=user_slug)
        grouping = get_object_or_404(Grouping, slug=group_slug, user=user)
        return grouping

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouping = self.object
        user = self.request.user
        is_owner = user.is_authenticated and grouping.user == user

        digits = grouping.get_digits(is_owner=is_owner, digit_type='all')

        context.update({
            'is_owner': is_owner,
            'pet_digits': digits.get('pets', []),
            'plant_digits': digits.get('plants', [])
        })

        return context
