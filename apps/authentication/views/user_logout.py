from django.contrib.auth.views import LogoutView


class UserLogout(LogoutView):
    next_page = '/'
