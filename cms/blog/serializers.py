from rest_framework import serializers
from wagtail.images.models import Image
from wagtail.images.api.fields import ImageRenditionField
from . import models

class BlogPageGalleryImageSerializer(serializers.ModelSerializer):
    image = ImageRenditionField('fill-100x100')

    class Meta:
        model = models.BlogPageGalleryImage
        fields = ['id', 'image', 'caption']

class BlogPageSerializer(serializers.ModelSerializer):
    gallery_images = BlogPageGalleryImageSerializer(many=True, read_only=True)
    main_image = ImageRenditionField('fill-100x100', source='main_image')
    authors = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'
    )
    tags = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'
    )

    class Meta:
        model = models.BlogPage
        fields = ['id', 'title', 'date', 'intro', 'body', 'authors', 'tags', 'gallery_images', 'main_image']
