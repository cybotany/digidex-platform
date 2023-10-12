from django.urls import path
from apps.itis.views import GetTSNView

app_name = 'itis'
urlpatterns = [
    path('get_tsn/', GetTSNView.as_view(), name='get-tsn'),
]
