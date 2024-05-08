from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class DigidexAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        """
        Returns the URL to redirect to after a successful email confirmation.
        """
        user_slug = request.user.username  # Ensure you are using the correct attribute for slug
        return reverse('profiles:update_user_profile', kwargs={'user_slug': user_slug})
