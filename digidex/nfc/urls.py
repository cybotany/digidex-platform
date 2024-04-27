from django.urls import include, path
from rest_framework.routers import DefaultRouter

from nfc import views

router = DefaultRouter()
router.register(r'nfc', views.NearFieldCommunicationTagViewSet, basename='nfc')

urlpatterns = [
    path('api/', include(router.urls)),
]
