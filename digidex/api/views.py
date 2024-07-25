from rest_framework import viewsets, status
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from api.serializers import NearFieldCommunicationTag, NearFieldCommunicationTagSerializer

User = get_user_model()


class NearFieldCommunicationTagViewSet(viewsets.ModelViewSet):
    queryset = NearFieldCommunicationTag.objects.all()
    serializer_class = NearFieldCommunicationTagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'serial_number'

    def create(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')
        owner_id = request.data.get('owner')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)

        if not owner_id:
            return Response({"error": "Owner not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            owner = User.objects.get(id=owner_id)
        except User.DoesNotExist:
            return Response({"error": "Owner not found."}, status=status.HTTP_404_NOT_FOUND)

        inventory_tag, created = NearFieldCommunicationTag.objects.get_or_create(
            serial_number=serial_number,
            defaults={'owner': owner}
        )

        # If the tag already exists, ensure it belongs to the provided owner
        if not created and inventory_tag.owner != owner:
            return Response({"error": "This serial number is already associated with a different owner."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(inventory_tag, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


inventory_router = DefaultRouter()
inventory_router.register('ntags', NearFieldCommunicationTagViewSet)
