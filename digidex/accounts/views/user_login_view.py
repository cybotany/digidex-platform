from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse
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
                login(self.request, user)
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
        # Check if there is a user-originating redirection URL and it's safe
        redirect_to = self.get_redirect_url()
        if redirect_to:
            return redirect_to
        else:
            # Use user's username_slug to construct the profile URL
            user_slug = self.request.user.username_slug
            return reverse('accounts:profile', kwargs={'username_slug': user_slug})

    def get_redirect_url(self):
        """Ensure the user-originating redirection URL is safe."""
        redirect_to = self.request.GET.get('next', '')
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts={self.request.get_host()},
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''
