from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from digidex.accounts.forms import LoginForm

class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        # Check if the user exists and has confirmed their email
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            if not user.email_confirmed:
                return self.form_invalid(form, "Please confirm your email address to log in.")
            else:
                return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form, error_message=None):
        """If the form is invalid, render the invalid form."""
        if error_message:
            form.add_error(None, error_message)
        return super().form_invalid(form)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_redirect_url(self):
        """Ensure the user-originating redirection URL is safe."""
        redirect_to = self.request.GET.get('next', '')
        url_is_safe = is_safe_url(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''
