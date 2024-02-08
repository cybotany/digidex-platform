from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages
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

    def form_valid(self, form):
        """
        If the form is valid, save the associated model and send a success message.
        """
        response = super().form_valid(form)
        messages.success(self.request, "Profile updated successfully.")
        return response

    def form_invalid(self, form):
        """
        If the form is invalid, add an error message before re-rendering the form.
        """
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")
        return super().form_invalid(form)

    def get_success_url(self):
        """
        After successfully updating the profile, redirect to the profile's URL.
        """
        return self.object.get_absolute_url()
