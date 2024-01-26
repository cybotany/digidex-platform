from rest_framework import serializers
from digidex.taxonomy.models import Unit


class TaxonomyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['tsn', 'complete_name']
