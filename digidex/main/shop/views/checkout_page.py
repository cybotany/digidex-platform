from django.views.generic import TemplateView


class CheckoutView(TemplateView):
    template_name = 'main/checkout-page.html'
