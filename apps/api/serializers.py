from rest_framework import serializers
from apps.botany.models import Plant, PlantImage
from apps.itis.models import TaxonomicUnits


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ['image', 'timestamp']


class TaxonomicUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomicUnits
        fields = ['tsn', 'complete_name']


class PlantSerializer(serializers.ModelSerializer):
    tsn = TaxonomicUnitsSerializer()
    images = PlantImageSerializer(many=True, read_only=True)
    get_absolute_url = serializers.SerializerMethodField()
    days_since_last_watering = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'added_on', 'nfc_tag', 'quantity', 'tsn', 'group', 'get_absolute_url', 'days_since_last_watering', 'images']
    
    def get_get_absolute_url(self, obj):
        # This method returns the absolute URL for the Plant instance.
        return obj.get_absolute_url()

    def get_days_since_last_watering(self, obj):
        # This method returns the days since the plant was last watered.
        return obj.days_since_last_watering()
