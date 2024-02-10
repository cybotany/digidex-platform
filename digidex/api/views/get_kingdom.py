from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from digidex.taxonomy.models import Kingdom

class GetKingdom(APIView):
    def get(self, request, id):
        kingdom = get_object_or_404(Kingdom, pk=id)
        # Assume these methods are defined to fetch the necessary data
        kingdom_data = {
            'valid_units_by_rank': kingdom.valid_units_by_rank(),
            'valid_units_by_geography': kingdom.valid_units_by_geography(),
            'valid_units_by_jurisdiction': kingdom.valid_units_by_jurisdiction(),
        }
        
        return Response(kingdom_data, status=status.HTTP_200_OK)
