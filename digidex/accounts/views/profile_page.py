from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from digidex.accounts.models import Profile

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-page.html'
    context_object_name = 'user_profile'
