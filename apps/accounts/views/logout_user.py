from django.contrib.auth.views import LogoutView


class LogoutUserView(LogoutView):
    next_page = 'landing-page'
