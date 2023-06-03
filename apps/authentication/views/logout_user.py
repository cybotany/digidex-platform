from django.contrib.auth.views import LogoutView


class LogoutUser(LogoutView):
    next_page = '/'
