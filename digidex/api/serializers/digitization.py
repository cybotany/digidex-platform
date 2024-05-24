from rest_framework import serializers

from digitization.models import DigitalObject


class DigitalObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalObject
        fields = ['id', 'name', 'description']
