from django.contrib.auth.models import User
from apps.botany.models import Plant
from apps.itis.models import TaxonomicUnits
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class TaxonomicUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomicUnits
        fields = ['tsn', 'complete_name']
