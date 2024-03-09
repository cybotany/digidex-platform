from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Project specific imports
from accounts import api

router = DefaultRouter()
router.register(r'users', api.DigidexUserViewSet)
router.register(r'profile', api.DigidexProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
