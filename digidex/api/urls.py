from rest_framework.routers import DefaultRouter
from django.urls import include, path

from api.views.digitization import DigitalObjectViewSet
from api.views.inventory import UserInventoryViewSet
from api.views.journal import JournalEntryViewSet
from api.views.nfc import RegisterNearFieldCommunicationTag
from api.views.party import UserPartyViewSet
from api.views.profiles import UserProfileViewSet
from api.views.tokens import UserTokenObtainPairView


router = DefaultRouter()
router.register('digitization', DigitalObjectViewSet, basename='digitization')
router.register('inventory', UserInventoryViewSet, basename='inventory')
router.register('journal', JournalEntryViewSet, basename='journal')
router.register('party', UserPartyViewSet, basename='party')
router.register('profiles', UserProfileViewSet, basename='profiles')

app_name = 'api'
urlpatterns = [
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('nfc/tag/registration/', RegisterNearFieldCommunicationTag.as_view(), name='register-ntag'),
    path('', include(router.urls)),
]
