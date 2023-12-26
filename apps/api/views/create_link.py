from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.inventory.models import Link


class CreateLink(APIView):
    permission_classes = [AllowAny]  # Or use appropriate permission classes

    def post(self, request, *args, **kwargs):
        uid = request.data.get('uid')
        if not uid:
            return Response({"error": "UID not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            link = Link.objects.create(serial_number=uid)
            return Response({"status": "success", "link_id": link.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
