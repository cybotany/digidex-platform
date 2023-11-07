from rest_framework import serializers
from apps.botany.models import Plant
from apps.itis.models import TaxonomicUnits

class TaxonomicUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomicUnits
        fields = ['tsn', 'complete_name']

class PlantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Assuming you want to represent the user as a string.
    tsn = TaxonomicUnitsSerializer()  # Nested serialization for related TaxonomicUnits.
    get_absolute_url = serializers.SerializerMethodField()
    days_since_last_watering = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = ['id', 'name', 'description', 'added_on', 'nfc_tag', 'quantity', 'tsn', 'group', 'get_absolute_url', 'days_since_last_watering']
    
    def get_get_absolute_url(self, obj):
        # This method returns the absolute URL for the Plant instance.
        return obj.get_absolute_url()

    def get_days_since_last_watering(self, obj):
        # This method returns the days since the plant was last watered.
        return obj.days_since_last_watering()

# Note that we have removed UserSerializer since it's not used in the PlantSerializer.
