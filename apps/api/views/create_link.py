from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.nfc.models import Link


class CreateLink(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        if not uid:
            return Response({"error": "UID not provided."}, status=status.HTTP_400_BAD_REQUEST)
        link, created = Link.objects.get_or_create(uid=uid)
        link_url = request.build_absolute_uri(link.get_absolute_url())
        return Response({"link_url": link_url}, status=status.HTTP_201_CREATED)
