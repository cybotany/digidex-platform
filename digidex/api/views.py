from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from nfc.models import NearFieldCommunicationTag

@method_decorator(csrf_exempt, name='dispatch')
class RegisterNearFieldCommunicationTag(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')

        if not serial_number:
            return Response({"error": "Serial Number not provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        ntag, created = NearFieldCommunicationTag.objects.update_or_create(
            serial_number=serial_number
        )
        ntag_url = request.build_absolute_uri(ntag.get_static_url())
        return Response({"ntag_url": ntag_url}, status=status.HTTP_201_CREATED)
