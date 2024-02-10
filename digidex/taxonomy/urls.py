from django.urls import path
from digidex.taxonomy.views import KingdomDetailsView

app_name = 'taxonomy'
urlpatterns = [
    path('kingdom/<int:kingdom_id>/', KingdomDetailsView.as_view(), name='kingdom-details'),
]
