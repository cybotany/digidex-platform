from django.urls import path
from .views import LinkingView

app_name = 'nfc'
urlpatterns = [
    path('link/', LinkingView.as_view(), name='linking'),
]
