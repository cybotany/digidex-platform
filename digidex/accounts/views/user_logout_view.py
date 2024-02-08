from django.contrib.auth.views import LogoutView


class UserLogoutView(LogoutView):
    next_page = 'main:landing'
