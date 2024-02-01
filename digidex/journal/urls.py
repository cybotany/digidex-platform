from django.urls import path
from digidex.journal.views import EntryCollectionView, EntryCreationView, EntryDetailView, EntryDeletionView

app_name = 'journal'
urlpatterns = [
    path('collection/<int:collection_id>/', EntryCollectionView.as_view(), name='collection-details'),
    path('collection/<int:collection_id>/add/', EntryCreationView.as_view(), name='add-entry'),

    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-details'),
    path('entry/<int:pk>/delete', EntryDeletionView.as_view(), name='delete-entry'),
]
