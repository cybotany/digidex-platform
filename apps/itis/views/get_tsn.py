from django.http import JsonResponse
from django.views import View
from apps.itis.models import TaxonomicUnits


class GetTSNView(View):
    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('q')
        tsn_objects = TaxonomicUnits.objects.filter(name__icontains=search_term)[:10]  # adjust the limit as needed
        results = [{"id": tsn.id, "text": tsn.name} for tsn in tsn_objects]
        return JsonResponse({"items": results})
