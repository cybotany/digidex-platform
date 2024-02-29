from django.views.generic.detail import DetailView
from digidex.inventory.models import Profile

class DetailProfile(DetailView):
    model = Profile
    template_name = 'inventory/profile/detail-page.html'
    context_object_name = 'profile'
    slug_field = 'user__slug'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = context['profile']
        is_profile_owner = self.request.user.is_authenticated and self.request.user == profile.user

        pet_digits = []
        pet_count = 0
        plant_digits = []
        plant_count = 0
        groupings = []

        if is_profile_owner or profile.is_public:
            user_groupings = profile.get_groupings()
            digits = profile.get_default_digits()

            groupings = user_groupings.get('groupings', [])
            grouping_count = user_groupings.get('grouping_count', 0)
            
            pet_digits = digits.get('digits', {}).get('pets', {}).get('items', [])
            pet_count = digits.get('digits', {}).get('pets', {}).get('count', 0)
            
            plant_digits = digits.get('digits', {}).get('plants', {}).get('items', [])
            plant_count = digits.get('digits', {}).get('plants', {}).get('count', 0)

        context.update({
            'is_profile_owner': is_profile_owner,
            'groupings': groupings,
            'grouping_count': grouping_count,
            'pet_digits': pet_digits,
            'pet_count': pet_count,
            'plant_digits': plant_digits,
            'plant_count': plant_count,
        })
        
        return context
