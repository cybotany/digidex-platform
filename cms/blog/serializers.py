from rest_framework import serializers as rf_serializers
from wagtail.images.api.fields import ImageRenditionField
# Project specific imports
from blog import models

class BlogPageGalleryImageSerializer(rf_serializers.ModelSerializer):
    image = ImageRenditionField('fill-100x100')

    class Meta:
        model = models.BlogPageGalleryImage
        fields = ['id', 'image', 'caption']


class AuthorSerializer(rf_serializers.ModelSerializer):
    author_image = ImageRenditionField('fill-100x100', allow_null=True)

    class Meta:
        model = models.Author
        fields = ['id', 'name', 'author_image']


class BlogPageSerializer(rf_serializers.ModelSerializer):
    gallery_images = BlogPageGalleryImageSerializer(many=True, read_only=True)
    main_image = ImageRenditionField('fill-100x100', source='main_image')
    authors = rf_serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'
    )
    tags = rf_serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'
    )

    class Meta:
        model = models.BlogPage
        fields = ['id', 'title', 'date', 'intro', 'body', 'authors', 'tags', 'gallery_images', 'main_image']
