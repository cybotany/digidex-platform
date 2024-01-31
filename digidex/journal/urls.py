from django.urls import path
from digidex.journal.views import DigitJournalView

app_name = 'journal'
urlpatterns = [
    path('digit/<str:serial_number>/journal', DigitJournalView.as_view(), name='digit-journal'),
]
