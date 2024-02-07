from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from digidex.utils.helpers import validate_recaptcha
from digidex.main.forms import ContactForm
import logging

logger = logging.getLogger(__name__)

class ContactView(FormView):
    template_name = 'main/contact-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:thanks')

    def form_valid(self, form):
        recaptcha_token = self.request.POST.get('g-recaptcha-response')
        validation_result = validate_recaptcha(recaptcha_token, 'contact_us')

        if not validation_result.get("success"):
            # Log the failure and add an error message
            logger.warning(f"reCAPTCHA validation failed: {validation_result.get('message')}")
            messages.error(self.request, "Invalid reCAPTCHA. Please try again.")

            # Instead of redirecting, treat the form as if it were invalid to stay on the page
            # and display the error message.
            return self.form_invalid(form)

        # If reCAPTCHA validation passes, proceed as normal.
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Optionally, log that the form was invalid or add additional error handling
        logger.info("Contact form submission was invalid.")
        return super().form_invalid(form)
