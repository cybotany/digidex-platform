from django.utils.text import slugify

from allauth.account.adapter import DefaultAccountAdapter


class DigidexAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return f"/{slugify(request.user.username)}/" 
