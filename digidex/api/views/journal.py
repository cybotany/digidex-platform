from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from journal.models import JournalEntry
from api.serializers.journal import JournalEntrySerializer


class JournalEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated]
