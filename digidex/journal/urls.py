from django.urls import path
from digidex.journal.views import EntryCollectionView, EntryCreationView, EntryDetailView, EntryDeletionView

app_name = 'journal'
urlpatterns = [
    path('collection/<int:pk>/', EntryCollectionView.as_view(), name='collection'),
    path('collection/<int:pk>/add/', EntryCreationView.as_view(), name='entry-creation'),

    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry'),
    path('entry/<int:pk>/delete', EntryDeletionView.as_view(), name='entry-deletion'),
]
