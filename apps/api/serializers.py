from rest_framework import serializers
from apps.botany.models import PlantImage
from apps.taxonomy.models import Units


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ['image', 'timestamp']


class taxonomyUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ['tsn', 'complete_name']
