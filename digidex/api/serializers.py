from rest_framework import serializers

from inventorytags.models import NearFieldCommunicationTag


class NearFieldCommunicationTagSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = NearFieldCommunicationTag
        fields = ['uuid', 'serial_number', 'active', 'created_at', 'last_modified', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_url())
