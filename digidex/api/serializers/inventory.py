from rest_framework import serializers

from inventory.models import Category

class CategorySerializer(serializers.ModelSerializer):
    detail_page_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['uuid', 'name', 'description', 'created_at', 'last_modified',]
