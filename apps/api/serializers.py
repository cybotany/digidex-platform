from rest_framework import serializers
from apps.taxonomy.models import Units


class TaxonomyUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ['tsn', 'complete_name']
