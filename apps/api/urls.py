from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.api.views import ChatbotAPIView, GetGroupView, GetTSNView

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chatbot/', ChatbotAPIView.as_view(), name='chatbot'),
    path('get_group/<int:group_id>/', GetGroupView.as_view(), name='get-group'),
    path('get_tsn/', GetTSNView.as_view(), name='get-tsn'),
]
