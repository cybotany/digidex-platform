from django.contrib.auth.forms import UserChangeForm

from apps.accounts.models import Profile


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date',)
