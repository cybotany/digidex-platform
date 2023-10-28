from django.urls import path
from apps.itis.views import GetTSNView, ITISHomepageView

app_name = 'itis'
urlpatterns = [
    path('', ITISHomepageView.as_view(), name='home'),
    path('get_tsn/', GetTSNView.as_view(), name='get-tsn'),
]
