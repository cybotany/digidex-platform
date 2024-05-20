from rest_framework import serializers

from inventory.models import UserInventory


class UserInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInventory
        fields = ['id', 'name', 'asset_items']
