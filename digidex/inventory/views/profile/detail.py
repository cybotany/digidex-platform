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

        if is_profile_owner or profile.is_public:
            user_groupings = profile.get_groupings(include=['counts', 'digits'], is_owner=is_profile_owner)
        else:
            user_groupings = []

        context.update({
            'is_profile_owner': is_profile_owner,
            'user_groupings': user_groupings,
        })
        
        return context
