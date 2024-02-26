from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.db.models import Q
from digidex.taxonomy.models import Unit
from digidex.api.serializers import TaxonomyUnitSerializer

class GetTSN(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('q', '').strip()
        kingdom_id = request.GET.get('kingdom_id', '')
    
        if not search_term:
            raise APIException("Search term is required.")
        
        if not kingdom_id.isdigit():
            raise APIException("Invalid kingdom_id. Please specify a valid kingdom_id.")

        tsn_objects = Unit.objects.filter(
            Q(complete_name__icontains=search_term) & 
            Q(kingdom__id=kingdom_id)
        )[:10]

        serialized_data = TaxonomyUnitSerializer(tsn_objects, many=True).data
        results = [{"id": tsn['tsn'], "text": tsn['complete_name']} for tsn in serialized_data]
        return Response({"items": results})
