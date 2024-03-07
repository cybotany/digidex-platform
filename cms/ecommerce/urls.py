from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cms.ecommerce import views

router = DefaultRouter()
router.register(r'shop', views.DigidexUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
