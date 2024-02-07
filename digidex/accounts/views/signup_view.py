from django.contrib import messages
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from digidex.utils.helpers import validate_recaptcha
from digidex.accounts.forms import SignupForm
from digidex.accounts.models import User
import logging

logger = logging.getLogger(__name__)

class SignupUserView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup-page.html'

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        validation_result = validate_recaptcha(recaptcha_response, 'signup')
        
        if validation_result.get("success"):
            user = form.save()
            user.send_verification_email
            return redirect('accounts:confirm-email')
        else:
            messages.error(self.request, "Invalid reCAPTCHA. Please try again.")
            logger.warning(f"reCAPTCHA validation failed: {validation_result.get('message')}")
            return self.form_invalid(form)

    def form_invalid(self, form):
        # You might want to add additional handling here in case of form invalidation
        # For example, logging or custom error messages
        return render(self.request, self.template_name, {'form': form})