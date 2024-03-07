from rest_framework import serializers
from .models import BlogPage, BlogPageGalleryImage
from wagtail.images.models import Image
from wagtail.images.api.fields import ImageRenditionField

class BlogPageGalleryImageSerializer(serializers.ModelSerializer):
    image = ImageRenditionField('fill-100x100')  # Adjust rendition spec as needed

    class Meta:
        model = BlogPageGalleryImage
        fields = ['id', 'image', 'caption']

class BlogPageSerializer(serializers.ModelSerializer):
    gallery_images = BlogPageGalleryImageSerializer(many=True, read_only=True)
    main_image = ImageRenditionField('fill-100x100', source='main_image')  # Adjust rendition spec as needed
    authors = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'  # Assuming 'name' is a field on your Author model
    )
    tags = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'
    )

    class Meta:
        model = BlogPage
        fields = ['id', 'title', 'date', 'intro', 'body', 'authors', 'tags', 'gallery_images', 'main_image']
