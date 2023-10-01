from django.urls import path
from apps.itis.views import KingdomDropdownView

app_name = 'itis'
urlpatterns = [
    path('kingdom/', KingdomDropdownView.as_view(), name='kingdom-dropdown'),
]
