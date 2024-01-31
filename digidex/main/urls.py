from django.urls import path
from digidex.main.views import (LandingView,
                                ContactUsView,
                                AboutUsView,
                                ThankYouView,
                                CheckoutView,
                                DetailCategoryView,
                                DetailPostView,
                                DetailProductView,
                                OrderConfirmationView,
                                PayPalCheckoutView,
                                PricingView,
                                SolutionsView,
                                BlogView)

app_name = 'main'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('company/', AboutUsView.as_view(), name='company'),
    path('thank-you/', ThankYouView.as_view(), name='thanks'),

    path('pricing', PricingView.as_view(), name='pricing'),
    path('solutions/', SolutionsView.as_view(), name='soltions'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post-detail/', DetailPostView.as_view(), name='post-detail'),

    path('category-detail/', DetailCategoryView.as_view(), name='category-detail'),
    path('product-detail/', DetailProductView.as_view(), name='product-detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('checkout/paypal/', PayPalCheckoutView.as_view(), name='checkout-paypal'),
    path('order-confirmation/', OrderConfirmationView.as_view(), name='order-confirmation'),
]
