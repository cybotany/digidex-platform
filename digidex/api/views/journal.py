from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from journal.models import Entry
from api.serializers.journal import JournalEntrySerializer


class JournalEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
