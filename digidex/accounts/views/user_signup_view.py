from django.contrib import messages
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from digidex.utils.helpers import validate_recaptcha
from digidex.accounts.forms import SignupForm
from digidex.accounts.models import User
import logging

logger = logging.getLogger(__name__)

class UserSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup-page.html'

    def form_valid(self, form):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        validation_result = validate_recaptcha(recaptcha_response, 'signup')
        
        if validation_result.get("success"):
            try:
                form.save()
                return redirect('accounts:confirm-email')
            except Exception as e:
                logger.error(f"Error during user signup and sending verification email: {e}")
                messages.error(self.request, "There was an error processing the signup form. Please try again later.")
                return self.form_invalid(form)
        else:
            messages.error(self.request, "Invalid reCAPTCHA. Please try again.")
            logger.error(f"reCAPTCHA validation failed: {validation_result.get('message')}")
            return self.form_invalid(form)

    def form_invalid(self, form):
        logger.info("Signup form submission was invalid.")
        return render(self.request, self.template_name, {'form': form})