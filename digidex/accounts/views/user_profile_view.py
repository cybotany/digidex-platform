from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.accounts.models import Profile
from digidex.inventory.models import Digit

class UserProfileView(LoginRequiredMixin, ListView):
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


class DigitStorageView(LoginRequiredMixin, ListView):
    model = Digit
    context_object_name = 'digits'
    template_name = 'inventory/digit-storage-page.html'

    def get_queryset(self):
        """ Overriding to get Digits for the current user """
        return Digit.objects.filter(nfc_link__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'subtitle': 'Storage',
            'heading': 'Storage Box n',
            'paragraph': 'Details about Storage Box n'
        })
        return context
