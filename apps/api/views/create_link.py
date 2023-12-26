from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.inventory.models import Link
from django.db import IntegrityError


class CreateLink(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        if not uid:
            return Response({"error": "UID not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            link, created = Link.objects.get_or_create(serial_number=uid)
            if created:
                return Response({"status": "success", "link_id": link.id}, status=status.HTTP_201_CREATED)
            else:
                # Logic for existing link can be added here later
                return Response({"status": "link already exists", "link_id": link.id}, status=status.HTTP_200_OK)
        except IntegrityError as e:
            # This block will execute if there's a database integrity issue, such as a unique constraint violation.
            return Response({"error": "Database integrity error - possibly duplicate UID."}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
