from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cms.accounts.views import user_viewset

router = DefaultRouter()
router.register(r'users', user_viewset.DigidexUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
