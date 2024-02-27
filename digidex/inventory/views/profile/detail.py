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
        """
        if is_profile_owner:
            user_pets = profile.get_user_pets()
            user_plants = profile.get_user_plants()
        elif profile.is_public:
            user_pets = profile.get_user_pets().filter(is_public=True)
            user_plants = profile.get_user_plants().filter(is_public=True)
        else:
            user_pets = []
            user_plants = []
        """
        user_pets = []
        user_plants = []
        pet_count = len(user_pets)
        plant_count = len(user_plants)

        context.update({
            'is_profile_owner': is_profile_owner,
            'pets': user_pets,
            'pet_count': pet_count,
            'plants': user_plants,
            'plant_count': plant_count,
        })
        
        return context
