from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register(r'users', views.DigidexUserViewSet)
router.register(r'profile', views.DigidexProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
