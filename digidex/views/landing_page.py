from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'main/landing-page.html'
