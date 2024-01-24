from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from digit.accounts.models import Profile
from digit.accounts.forms import ProfileForm


class ModifyProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'main/profile-modification-page.html'

    def get_object(self, queryset=None):
        """
        This view will edit the profile associated with the current user.
        """
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        """
        After successfully updating the profile, redirect to the user's profile page.
        """
        return reverse_lazy('accounts:profile', kwargs={'pk': self.request.user.pk})
