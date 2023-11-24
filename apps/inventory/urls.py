from django.urls import path
from .views import HandleLinkView

app_name = 'inventory'
urlpatterns = [
    path('link/<str:secret_hash>/', HandleLinkView.as_view(), name='link-handling'),
]
