from django.urls import path
from digidex.journal.views import (DetailCollection,
                                   AddEntry, DetailEntry, DeleteEntry)

app_name = 'journal'
urlpatterns = [
    path('collection/<int:pk>/', DetailCollection.as_view(), name='detail-collection'),
    
    path('collection/<int:pk>/add/', AddEntry.as_view(), name='add-entry'),
    path('entry/<int:pk>/', DetailEntry.as_view(), name='detail-entry'),
    path('entry/<int:pk>/delete/', DeleteEntry.as_view(), name='delete-entry'),
]
