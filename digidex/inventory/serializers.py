from rest_framework import serializers

from ..nfc.models import NearFieldCommunicationTag, NearFieldCommunicationLink


class NearFieldCommunicationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearFieldCommunicationTag
        fields = '__all__'


class NearFieldCommunicationLinkSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(write_only=True)

    class Meta:
        model = NearFieldCommunicationLink
        fields = '__all__'
