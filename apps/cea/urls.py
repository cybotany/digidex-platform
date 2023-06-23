from django.urls import path
from apps.cea.views import CEAHomepageView, FindCEAView, RegisterGrowthChamberView, RegisterGreenhouseView, RegisterTissueCultureChamberView

app_name = 'cea'
urlpatterns = [
    path('', CEAHomepageView.as_view(), name='home'),
    path('find-cea/', FindCEAView.as_view(), name='find_cea'),
    path('new-growth-chamber/', RegisterGrowthChamberView.as_view(), name='new_growth_chamber'),
    path('new-greenhouse/', RegisterGreenhouseView.as_view(), name='new_greenhouse'),
    path('new-tissue-culture-chamber/', RegisterTissueCultureChamberView.as_view(), name='new_tissue_culture_chamber'),
]
