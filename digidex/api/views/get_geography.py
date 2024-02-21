from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from digidex.taxonomy.models import Geography

class GetGeography(APIView):
    def get(self, request, id):
        geography = get_object_or_404(Geography, pk=id)

        geography_data = {
            'valid_protozoa_units': geography.valid_protozoa_units(),
            'valid_plantae_units': geography.valid_plantae_units(),
            'valid_animalia_units': geography.valid_animalia_units(),
            'valid_chromista_units': geography.valid_chromista_units(),
        }
        
        return Response(geography_data, status=status.HTTP_200_OK)
