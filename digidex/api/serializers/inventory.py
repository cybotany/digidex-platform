from rest_framework import serializers

from inventory.models import UserInventory

class UserInventorySerializer(serializers.ModelSerializer):
    detail_page_url = serializers.SerializerMethodField()

    class Meta:
        model = UserInventory
        fields = ['uuid', 'name', 'description', 'created_at', 'last_modified', 'detail_page_url']

    def get_detail_page_url(self, obj):
        if obj.detail_page:
            return obj.detail_page.url
        return None
