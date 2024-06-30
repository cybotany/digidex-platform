from wagtail.api.v2.serializers import PageSerializer

from .models import AssetPage


class AssetPageSerializer(PageSerializer):
    class Meta:
        model = AssetPage
        fields = ['id', 'title', 'slug', 'uuid', 'url', 'description']
