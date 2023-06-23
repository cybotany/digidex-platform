from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.cea.models import Greenhouse


@method_decorator(csrf_exempt, name='dispatch')
class CEAMappingAPIView(APIView):

    def post(self, request):
        ip_address = request.data.get('ip_address')
        identifier = request.data.get('identifier')

        if not ip_address or not identifier:
            return Response({'error': 'Missing ip_address or identifier.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a Greenhouse with the given identifier already exists
        greenhouse = Greenhouse.objects.filter(identifier=identifier).first()

        if greenhouse:
            # If it does, update the IP address
            greenhouse.ip_address = ip_address
            greenhouse.save()
        else:
            # If it doesn't, create a new Greenhouse
            greenhouse = Greenhouse.objects.create(ip_address=ip_address, identifier=identifier)

        # You can do more things here like associating the IP with a user or a specific device
        return Response({'message': 'CEA successfully registered.', 'greenhouse_id': greenhouse.id}, status=status.HTTP_200_OK)
