from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from api.views.digitization import UserDigitViewSet
from api.views.inventory import UserInventoryViewSet
from api.views.journal import JournalEntryViewSet
from api.views.nfc import RegisterNearFieldCommunicationTag
from api.views.party import UserPartyViewSet
from api.views.profiles import UserProfileViewSet

jwt_urls = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#router = DefaultRouter()
#router.register('digitization', UserDigitViewSet)
#router.register('inventory', UserInventoryViewSet)
#router.register('journal', JournalEntryViewSet)
#router.register('party', UserPartyViewSet)
#router.register('profiles', UserProfileViewSet)


app_name = 'api'
urlpatterns = [
    path('token/', include(jwt_urls)),
    path('nfc/tag/registration/', RegisterNearFieldCommunicationTag.as_view(), name='register-ntag'),
]
