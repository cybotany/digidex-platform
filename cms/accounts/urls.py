from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cms.accounts import serializers

router = DefaultRouter()
router.register(r'users', serializers.DigidexUserSerializer)

urlpatterns = [
    path('api/', include(router.urls)),
]
