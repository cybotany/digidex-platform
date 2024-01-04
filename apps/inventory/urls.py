from django.urls import path
from .views import (DigitStorageView, DigitDetailsView, DigitDeletionView)

app_name = 'inventory'
urlpatterns = [
    path('', DigitStorageView.as_view(), name='storage'),
    path('<int:pk>', DigitDetailsView.as_view(), name='details'),
    path('delete/<int:pk>', DigitDeletionView.as_view(), name='deletion'),
]
