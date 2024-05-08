from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse


class DigidexAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_redirect_url(self, request):
        """
        Returns the URL to redirect to after a successful email confirmation.
        """
        return reverse('profiles:update_user_profile')
