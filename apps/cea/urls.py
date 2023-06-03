from django.urls import path
from .views import RegisterGrowthChamber, DisplayGrowthChamber

urlpatterns = [
    path('growth_chamber', DisplayGrowthChamber.as_view(), name='growth_chamber'),
    path('register_growth_chamber', RegisterGrowthChamber.as_view(), name='register_growth_chamber'),
]
