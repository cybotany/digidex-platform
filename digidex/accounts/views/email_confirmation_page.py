from django.views.generic import TemplateView


class EmailConfirmationView(TemplateView):
    template_name = 'main/email-confirmation-page.html'
