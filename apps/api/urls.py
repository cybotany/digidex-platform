from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.api.views import GetGroup, GetTSN, CreateLink

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get/group/<int:group_id>/', GetGroup.as_view(), name='get-group'),
    path('get/tsn/', GetTSN.as_view(), name='get-tsn'),
    path('create/link/<str:uid>/', CreateLink.as_view(), name='create-link'),
]
