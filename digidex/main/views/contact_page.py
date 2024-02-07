from django.contrib import messages
from django.http import HttpResponseRedirect
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
            messages.error(self.request, "Invalid reCAPTCHA. Please try again.")
            logger.warning(f"reCAPTCHA validation failed: {validation_result.get('message')}")
            return HttpResponseRedirect(reverse_lazy('main:error'))

        form.save()
        return super().form_valid(form)
