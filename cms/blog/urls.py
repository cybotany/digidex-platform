from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cms.blog import api

router = DefaultRouter()
router.register(r'blogs', api.DigidexUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
