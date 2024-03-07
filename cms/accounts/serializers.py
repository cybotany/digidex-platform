from rest_framework import serializers
from cms.accounts.models import user

class DigidexUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.DigidexUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']


class DigidexProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.DigidexProfile
        fields = ['user_id', 'bio', 'location', 'avatar', 'is_public', 'created_at', 'last_modified']