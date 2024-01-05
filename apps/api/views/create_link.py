from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.nfc.models import Link
from django.db import IntegrityError


class CreateLink(APIView):
    permission_classes = [AllowAny]  # [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        if not uid:
            return Response({"error": "UID not provided."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            link, created = Link.objects.get_or_create(uid=uid)
            if created:
                # Link created successfully, return the URL for this link
                link_url = request.build_absolute_uri(link.get_absolute_url())
                return Response({"link_url": link_url}, status=status.HTTP_201_CREATED)
            else:
                return Response({"link_url": link_url}, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response({"error": "Database integrity error - possibly duplicate UID."}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
