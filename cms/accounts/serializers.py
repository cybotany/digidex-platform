from rest_framework import serializers
from cms.accounts.models import user

class DigidexUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.DigidexUser
        fields = ['id', 'username', 'email']
