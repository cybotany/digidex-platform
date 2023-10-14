from django.http import JsonResponse
from django.views import View
from apps.itis.models import TaxonomicUnits


class GetTSNView(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('q')
        tsn_objects = TaxonomicUnits.objects.filter(name__icontains=search_term)[:10]
        results = [{"id": tsn.tsn, "text": tsn.complete_name} for tsn in tsn_objects]
        return JsonResponse({"items": results})
