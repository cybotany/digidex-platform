from django.views.generic import TemplateView


class EmailSentView(TemplateView):
    template_name = 'accounts/email-confirmation-page.html'
