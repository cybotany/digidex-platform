from allauth.account.adapter import DefaultAccountAdapter


class DigidexAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return f"/u/{request.user.slug}/" 
