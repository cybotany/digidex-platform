from django.urls import path
from apps.nfc.views import RegisterTagView

app_name = 'nfc'
urlpatterns = [
    path('register/<str:pk>/', RegisterTagView.as_view(), name='tag-registration'),
]
