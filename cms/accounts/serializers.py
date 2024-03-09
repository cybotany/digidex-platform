from rest_framework import serializers
# Project specific imports
from accounts import models

class DigidexUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DigidexUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']


class DigidexProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DigidexProfile
        fields = ['user_id', 'bio', 'location', 'avatar', 'is_public', 'created_at', 'last_modified']