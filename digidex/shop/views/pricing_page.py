from django.views.generic import TemplateView


class PricingView(TemplateView):
    template_name = 'main/pricing-page.html'
