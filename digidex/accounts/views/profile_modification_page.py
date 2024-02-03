from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from digidex.accounts.models import Profile
from digidex.accounts.forms import ProfileForm


class ModifyProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile-modification-page.html'

    def get_object(self, queryset=None):
        """
        This view will edit the profile associated with the user ID passed in the URL.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, pk=pk)

    def get_success_url(self):
        """
        After successfully updating the profile, redirect to the profile's URL.
        """
        return self.object.get_absolute_url()
