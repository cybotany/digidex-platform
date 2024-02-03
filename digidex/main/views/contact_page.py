from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from digidex.main.forms import ContactForm

class ContactView(FormView):
    template_name = 'main/contact-page.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'subtitle': 'Contact Us',
            'heading': "Have questions? Contact us for assistance",
            'paragraph': "We're here to help!"
        })
        return context

    def form_valid(self, form):
        # Here you can add the logic to handle a valid form (e.g., sending an email)
        return super().form_valid(form)
