from django.views import View
from django.http import JsonResponse
from apps.itis.models import TaxonomicUnits


class GetPlantTSN(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('q')
        tsn_objects = TaxonomicUnits.objects.filter(complete_name__icontains=search_term)[:10]
        results = [{"id": tsn.tsn, "text": tsn.complete_name} for tsn in tsn_objects]
        return JsonResponse({"items": results})
