from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.accounts.models import Profile

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-page.html'
    context_object_name = 'user_profile'

    # Permission check
    def get_object(self, queryset=None):
        profile = super().get_object(queryset)
        if profile.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this profile.")
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_profile = context.get('user_profile')
        user = user_profile.user
    
        context.update({
            'subtitle': 'Profile',
            'date': user.date_joined.strftime("%b %d, %Y"),
            'heading': user.username,
            'paragraph': 'Details about Profile'
        })
        return context