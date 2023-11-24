from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
from apps.taxonomy.models import Units
from apps.api.serializers import TaxonomyUnitsSerializer


class GetTSN(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('q')
        tsn_objects = Units.objects.filter(complete_name__icontains=search_term)[:10]
        
        # Serialize data using DRF serializer
        serialized_data = TaxonomyUnitsSerializer(tsn_objects, many=True).data
        
        results = [{"id": tsn['tsn'], "text": tsn['complete_name']} for tsn in serialized_data]
        return Response({"items": results})


