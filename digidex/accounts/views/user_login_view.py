
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.shortcuts import resolve_url
from django.utils.http import url_has_allowed_host_and_scheme
from digidex.accounts.forms import LoginForm


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            if not user.email_confirmed:
                messages.error(self.request, "Please confirm your email address to log in.")
                return self.form_invalid(form)
            else:
                messages.success(self.request, "Login successful. Welcome back!")
                return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid login credentials.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        """If the form is invalid, simply render the invalid form without modifying it."""
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")
        return super().form_invalid(form)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_redirect_url(self):
        """Ensure the user-originating redirection URL is safe."""
        redirect_to = self.request.GET.get('next', '')
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts={self.request.get_host()},
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''
