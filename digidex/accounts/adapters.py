from allauth.account.adapter import DefaultAccountAdapter

from accounts.utils import create_user_profile


class DigidexAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        """
        Returns the URL to redirect to after a successful email confirmation.
        """
        user_profile = create_user_profile(request.user)
        user_profile_page = user_profile.create_profile_page()
        return user_profile_page.get_url()
