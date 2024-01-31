from django.urls import path
from digidex.main.views import (BlogView,
                                CheckoutView,
                                CompanyView,
                                ContactUsView,
                                DetailCategoryView,
                                DetailPostView,
                                DetailProductView,
                                DetailSKUView,
                                LandingView,
                                OrderConfirmationView,
                                PayPalCheckoutView,
                                PricingView,
                                SolutionsView,
                                ThankYouView)

app_name = 'main'
urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('company/', CompanyView.as_view(), name='company'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('category-detail/', DetailCategoryView.as_view(), name='detail-category'),
    path('post-detail/', DetailPostView.as_view(), name='detail-post'),
    path('product-detail/', DetailProductView.as_view(), name='detail-product'),
    path('sku-detail/', DetailSKUView.as_view(), name='detail-sku'),
    path('order-confirmation/', OrderConfirmationView.as_view(), name='order-confirmation'),
    path('checkout/paypal/', PayPalCheckoutView.as_view(), name='paypal-checkout'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('solutions/', SolutionsView.as_view(), name='solutions'),
    path('thank-you/', ThankYouView.as_view(), name='thanks'),
]
