from wagtail.api.v2.serializers import PageSerializer

from .models import InventoryPage


class InventoryPageSerializer(PageSerializer):
    class Meta:
        model = InventoryPage
        fields = ['id', 'title', 'slug', 'uuid', 'url', 'description']
