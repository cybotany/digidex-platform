from django.contrib.auth.views import LogoutView

class AccountLogoutView(LogoutView):
    next_page = '/'
