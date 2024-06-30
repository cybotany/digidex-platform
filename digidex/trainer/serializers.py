from wagtail.api.v2.serializers import PageSerializer

from .models import TrainerPage

class TrainerPageSerializer(PageSerializer):
    class Meta:
        model = TrainerPage
        fields = ['id', 'title', 'slug', 'uuid', 'url', 'introduction']
