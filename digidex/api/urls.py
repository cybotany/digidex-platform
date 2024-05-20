from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include, path

from api.views import (
    digitization as digitization_api,
    inventory as inventory_api,
    journal as journal_api,
    nfc as nfc_api,
    party as party_api,
    profiles as profiles_api,
)

jwt_urls = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#digitization_urls = [
#    path('', digitization_api.DigitizationListView.as_view(), name='digitization-list'),
#    path('<int:pk>/', digitization_api.DigitizationDetailView.as_view(), name='digitization-detail'),
#]

#inventory_urls = [
#    path('', inventory_api.UserInventoryListView.as_view(), name='inventory-list'),
#    path('<int:pk>/', inventory_api.UserInventoryDetailView.as_view(), name='inventory-detail'),
#]

#journal_urls = [
#    path('', journal_api.JournalListView.as_view(), name='journal-list'),
#    path('<int:pk>/', journal_api.JournalDetailView.as_view(), name='journal-detail'),
#]

nfc_urls = [
    path('register/', nfc_api.RegisterNearFieldCommunicationTag.as_view(), name='register-ntag'),
]

#party_urls = [
#    path('', party_api.PartyListView.as_view(), name='party-list'),
#    path('party/<int:pk>/', party_api.PartyDetailView.as_view(), name='party-detail'),
#]

#profiles_urls = [
#    path('', profiles_api.UserProfileListView.as_view(), name='profile-list'),
#    path('<int:pk>/', profiles_api.UserProfileDetailView.as_view(), name='profile-detail'),
#]

app_name = 'api'
urlpatterns = [
    path('token/', include(jwt_urls)),
#    path('inventory/', include(inventory_urls)),
#    path('journal/', include(journal_urls)),
    path('nfc/', include(nfc_urls)),
#    path('party/', include(party_urls)),
#    path('profiles/', include(profiles_urls)),
]
