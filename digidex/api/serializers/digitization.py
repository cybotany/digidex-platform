from rest_framework import serializers

from digitization.models import UserDigit


class UserDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDigit
        fields = ['id', 'name', 'description']
