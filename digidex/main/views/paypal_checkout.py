from django.views.generic import TemplateView


class PayPalCheckoutView(TemplateView):
    template_name = 'main/paypal_checkout.html'
