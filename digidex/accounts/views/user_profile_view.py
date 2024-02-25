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
        
        # Checks if the profile is public or if the user is authenticated and the owner of the profile.
        if profile.is_public or (self.request.user.is_authenticated and self.request.user == profile.user):
            user_digits = profile.get_user_digits()
            context['digits'] = user_digits
            context['digits_count'] = user_digits.count()
        else:
            context['digits'] = []
            context['digits_count'] = 0
            if not profile.is_public:
                context['private_profile'] = True
        
        context.update({
            'subtitle': 'Profile',
            'heading': f"{profile.user.username}",
            'paragraph': profile.bio,
            'date': profile.created_at,
        })
        return context
