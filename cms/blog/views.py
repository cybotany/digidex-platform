from rest_framework import viewsets
from .models import BlogPage
from .serializers import BlogPageSerializer

class BlogPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPage.objects.all()
    serializer_class = BlogPageSerializer

    def get_queryset(self):
        return super().get_queryset().live().order_by('-date')
