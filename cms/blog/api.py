from rest_framework import viewsets
from cms.blog import models, serializers

class DigidexBlogViewSet(viewsets.ModelViewSet):
    queryset = models.DigidexUser.objects.all()
    serializer_class = serializers.DigidexUserSerializer
