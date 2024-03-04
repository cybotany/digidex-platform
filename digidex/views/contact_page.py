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

        if validation_result.get("success"):
            try:
                form.save()
                return super().form_valid(form)
            except Exception as e:
                logger.error(f"Error during contact us email submission: {e}")
                messages.error(self.request, "There was an error processing the contact us form. Please try again later.")
                return self.form_invalid(form)
        
        else:
            # Log the failure and add an error message
            logger.error(f"reCAPTCHA validation failed: {validation_result.get('message')}")
            messages.error(self.request, "Invalid reCAPTCHA. Please try again.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        logger.info("Contact form submission was invalid.")
        return super().form_invalid(form)
