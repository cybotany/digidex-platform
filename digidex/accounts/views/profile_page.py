from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from digidex.accounts.models import Profile

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-page.html'
    context_object_name = 'user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_profile = context.get('user_profile')
        user = user_profile.user

        context['subtitle'] = 'Profile'
        context['heading'] = user.username
        context['date'] = user.date_joined.strftime("%b %d, %Y")
        context['paragraph'] = 'Details about Profile'

        return context