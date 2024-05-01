# adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_redirect_url(self, request):
        """
        Returns the URL to redirect to after a successful email confirmation.
        """
        if hasattr(request.user, 'profile'):
            return reverse('profile_update')
        else:
            return reverse('profile_create')
