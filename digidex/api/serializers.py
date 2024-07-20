from rest_framework import serializers

from inventory.models import InventoryTag


class InventoryTagSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = InventoryTag
        fields = ['serial_number', 'active', 'created_at', 'last_modified', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.get_url())
