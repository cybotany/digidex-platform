from django.views.generic import TemplateView


class EmailConfirmationView(TemplateView):
    template_name = 'accounts/email_confirmation.html'
