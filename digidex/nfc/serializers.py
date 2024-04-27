from rest_framework import serializers

from nfc import models

class NearFieldCommunicationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NearFieldCommunicationTag
        fields = '__all__'
