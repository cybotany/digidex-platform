from rest_framework import viewsets
from blog import models, serializers

class BlogPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.BlogPage.objects.all()
    serializer_class = serializers.BlogPageSerializer

    def get_queryset(self):
        return super().get_queryset().live().order_by('-date')
