from django.urls import path
from apps.taxonomy.views import HomepageView

app_name = 'taxonomy'
urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
]
