from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'plants', views.PlantViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
