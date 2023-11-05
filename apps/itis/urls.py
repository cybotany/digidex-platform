from django.urls import path
from apps.itis.views import ITISHomepageView

app_name = 'itis'
urlpatterns = [
    path('', ITISHomepageView.as_view(), name='home'),
]
