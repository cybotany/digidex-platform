from django.views.generic import TemplateView

class VerificationEmail(TemplateView):
    template_name = 'accounts/verification/email-page.html'
