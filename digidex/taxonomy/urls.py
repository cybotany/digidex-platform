from django.urls import path
from digidex.taxonomy.views import KingdomDetailView

app_name = 'taxonomy'
urlpatterns = [
    path('kingdoms/', KingdomDetailView.as_view(), name='kingdom-detail'),
]
