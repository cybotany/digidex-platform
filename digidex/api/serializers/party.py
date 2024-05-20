from rest_framework import serializers

from party.models import UserParty


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserParty
        fields = ('id', 'uuid',)
