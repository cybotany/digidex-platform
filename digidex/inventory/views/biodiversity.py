from django.http import JsonResponse

from inventory.models import GBIFSpecies


def species_autocomplete(request):
    query = request.GET.get('query', '')
    if query:
        response = GBIFSpecies.name_suggest(q=query, limit=10)
        suggestions = [{'taxon_id': item['key'], 'name': item['scientificName']} for item in response]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)
