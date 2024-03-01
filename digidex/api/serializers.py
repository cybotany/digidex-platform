from rest_framework import serializers

from digidex.taxonomy.models.taxon import base as base_taxon


class TaxonFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = base_taxon.Taxon
        fields = ['tsn', 'complete_name']
