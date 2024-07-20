from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.serializers import InventoryTag, InventoryTagSerializer


class InventoryTagViewSet(viewsets.ModelViewSet):
    queryset = InventoryTag.objects.all()
    serializer_class = InventoryTagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'serial_number'

    def create(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)

        inventory_tag, created = InventoryTag.objects.get_or_create(
            serial_number=serial_number
        )

        serializer = self.get_serializer(inventory_tag, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
