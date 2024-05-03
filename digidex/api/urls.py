from django.urls import path

from api.views import RegisterNearFieldCommunicationTag

urlpatterns = [
    path('register/ntag/', RegisterNearFieldCommunicationTag.as_view(), name='register-ntag'),
]
