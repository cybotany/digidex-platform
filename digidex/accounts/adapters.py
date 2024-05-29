from allauth.account.adapter import DefaultAccountAdapter


class DigidexAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        """
        Returns the URL to redirect to after a successful email confirmation.
        """
        user = request.user
        user_profile = user.create_profile()
        user_page = user.create_page()
        return user_page.page.url()
