from rest_framework import serializers

from home.models import NearFieldCommunicationTag


class NearFieldCommunicationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearFieldCommunicationTag
        fields = ['id', 'uuid', 'serial_number', 'ntag_type', 'digit', 'active', ]