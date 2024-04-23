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
        is_owner = self.request.user.is_authenticated and self.request.user == digit.ntag.user

        parent = digit.get_parent_details()
        parent_url = parent.get('url', '#')
        parent_name = parent.get('name', '')

        journal_entries = []

        if is_owner or digit.is_public:
            journal_entries = digit.get_journal_entries()
        
        context.update({
            'is_owner': is_owner,
            'parent_url': parent_url,
            'parent_name': parent_name,
            'journal_entries': journal_entries,
        })

        return context


from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from digidex.inventory.models import Grouping

class DetailGrouping(DetailView):
    model = Grouping
    template_name = 'inventory/grouping/detail-page.html'
    context_object_name = 'grouping'

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
        is_owner = self.request.user.is_authenticated and grouping.user == self.request.user

        parent = grouping.get_parent_details()
        parent_url = parent.get('url', '#')
        parent_name = parent.get('name', '')

        pet_digits = []
        pet_count = 0
        plant_digits = []
        plant_count = 0 

        if is_owner or grouping.is_public:
            digits = grouping.get_digits()

            pet_digits = digits.get('pets', {}).get('items', [])
            pet_count = digits.get('pets', {}).get('count', 0)

            plant_digits = digits.get('plants', {}).get('items', [])
            plant_count = digits.get('plants', {}).get('count', 0)

        context.update({
            'is_owner': is_owner,
            'parent_url': parent_url,
            'parent_name': parent_name,
            'pet_digits': pet_digits,
            'pet_count': pet_count,
            'plant_digits': plant_digits,
            'plant_count': plant_count
        })

        return context

