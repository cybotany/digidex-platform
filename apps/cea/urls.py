from django.urls import path
from .views import CEAHome, RegisterGrowthChamber, RegisterGreenhouse, RegisterTissueCultureChamber

app_name = 'cea'
urlpatterns = [
    path('', CEAHome.as_view(), name='home'),
    path('new_growth_chamber', RegisterGrowthChamber.as_view(), name='new_growth_chamber'),
    path('new_greenhouse', RegisterGreenhouse.as_view(), name='new_greenhouse'),
    path('new_tissue_culture_chamber', RegisterTissueCultureChamber.as_view(), name='new_tissue_culture_chamber'),
]
