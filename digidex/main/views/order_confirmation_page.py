from django.views.generic import TemplateView


class OrderConfirmationView(TemplateView):
    template_name = 'main/order-confirmation.html'
