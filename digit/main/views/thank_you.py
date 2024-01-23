from django.views.generic import TemplateView


class ThankYouView(TemplateView):
    template_name = 'main/thank-you.html'
