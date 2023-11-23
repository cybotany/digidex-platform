from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.api.views import GetPlantGroup, GetPlantTSN

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_plant_group/<int:group_id>/', GetPlantGroup.as_view(), name='get-plant-group'),
    path('get_plant_tsn/', GetPlantTSN.as_view(), name='get-plant-tsn'),
]
