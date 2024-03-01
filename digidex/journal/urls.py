from django.urls import path
from digidex.journal.views import (DetailJournalCollection, AddJournalEntry, DetailJournalEntry, DeleteJournalEntry)

app_name = 'journal'
urlpatterns = [
    path('collection/<int:pk>/', DetailJournalCollection.as_view(), name='detail-collection'), 
    path('collection/<int:pk>/add/', AddJournalEntry.as_view(), name='add-entry'),
    path('entry/<int:pk>/', DetailJournalEntry.as_view(), name='detail-entry'),
    path('entry/<int:pk>/delete/', DeleteJournalEntry.as_view(), name='delete-entry'),
]
