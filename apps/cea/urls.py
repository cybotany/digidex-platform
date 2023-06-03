from django.urls import path
from cea.views import GrowthChamberRegistrationView, UserGrowthChamberView

urlpatterns = [
    path('user_growth_chamber', UserGrowthChamberView.as_view(), name='user_growth_chamber'),
    path('growth_chamber_registration', GrowthChamberRegistrationView.as_view(), name='growth_chamber_registration'),
]
