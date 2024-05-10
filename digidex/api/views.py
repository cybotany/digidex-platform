from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from nfc.models import NearFieldCommunicationTag
# from inventory.models import UserDigitizedObject
# from inventory.serializers import UserDigitizedObjectSerializer                                                                                                             


class RegisterNearFieldCommunicationTag(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)

        ntag, created = NearFieldCommunicationTag.objects.update_or_create(
            serial_number=serial_number,
            defaults={'active': True}
        )

        _url = request.build_absolute_uri(ntag.get_absolute_url())
        _status = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        return Response({"ntag_url": _url}, status=_status)


# class UserDigitizedObjectViewSet(viewsets.ModelViewSet):
#    queryset = UserDigitizedObject.objects.all()
#    serializer_class = UserDigitizedObjectSerializer
