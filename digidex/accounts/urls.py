from django.urls import path, include

from accounts.api import urlpatterns as urlpatterns

urlpatterns += [
    path('', include('allauth.urls')),
]
