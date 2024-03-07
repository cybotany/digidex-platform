from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cms.accounts import api

router = DefaultRouter()
router.register(r'users', api.DigidexUserSerializer)

urlpatterns = [
    path('api/', include(router.urls)),
]
