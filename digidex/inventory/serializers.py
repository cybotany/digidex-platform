from rest_framework import serializers

from .models import NearFieldCommunicationTag


class NearFieldCommunicationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearFieldCommunicationTag
        fields = '__all__'
