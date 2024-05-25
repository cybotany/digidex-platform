from rest_framework import serializers

from journal.models import Entry


class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'caption',]
