from django.urls import path

from journal.views import add_digit_note

app_name = 'journal'
urlpatterns = [
    path('add/digit/<uuid:digit_uuid>/note/', add_digit_note, name='add_digit_note'),
]
