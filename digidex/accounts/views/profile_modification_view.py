from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.accounts.models import Profile
from digidex.accounts.forms import ProfileForm


class ProfileModificationView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile-modification-page.html'

    def get_object(self, queryset=None):
        """
        Only allow editing the profile associated with the currently logged-in user.
        """
        profile = super().get_object(queryset)
        if profile.user != self.request.user:
            raise PermissionDenied("You do not have permission to modify this profile.")
        return profile

    def get_success_url(self):
        """
        After successfully updating the profile, redirect to the profile's URL.
        """
        return self.object.get_absolute_url()
