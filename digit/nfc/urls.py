from django.urls import path
from .views import LinkingView

app_name = 'digit.nfc'
urlpatterns = [
    path('<uuid:uuid>/', LinkingView.as_view(), name='linking'),
]
