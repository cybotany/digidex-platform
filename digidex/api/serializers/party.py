from rest_framework import serializers

from party.models import UserParty


class UserPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserParty
        fields = ('id', 'uuid',)
