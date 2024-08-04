from django.utils.text import slugify

from allauth.account.adapter import DefaultAccountAdapter


class DigidexAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        """
        Returns the default URL to redirect to after logging in.
        Note that URLs passed explicitly (e.g. by passing along a next GET parameter)
        take precedence over the value returned here.
        """
        return f"/inv/{slugify(request.user.username)}/" 

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse
        """
        return False