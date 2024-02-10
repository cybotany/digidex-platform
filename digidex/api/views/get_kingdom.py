from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from digidex.taxonomy.models import Kingdom


class GetKingdom(APIView):
    """
    Retrieve details of a specific kingdom.
    """
    def get(self, request, id):
        kingdom = get_object_or_404(Kingdom, pk=id)
        # Serialize kingdom data to JSON
        data = {
            'kingdom_name': kingdom.kingdom_name,
        }
        return Response(data, status=status.HTTP_200_OK)
