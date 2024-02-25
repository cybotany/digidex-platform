from django.views.generic.detail import DetailView
from digidex.accounts.models import Profile


class UserProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile-page.html'
    context_object_name = 'profile'
    slug_field = 'user__username_slug'
    slug_url_kwarg = 'username_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = context['profile']

        is_profile_owner = self.request.user.is_authenticated and self.request.user == profile.user
        
        if profile.is_public or is_profile_owner:
            user_digits = profile.get_user_digits()
            digits_count = user_digits.count()
        else:
            user_digits = []
            digits_count = 0

        context.update({
            'is_profile_owner': is_profile_owner,
            'digits': user_digits,
            'digits_count': digits_count,
        })
        
        return context
