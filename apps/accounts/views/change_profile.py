from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.accounts.models import Profile
from apps.accounts.forms import ProfileChangeForm


class ChangeProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileChangeForm
    template_name = 'accounts/change_profile.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self, queryset=None):
        return self.request.user.profile
