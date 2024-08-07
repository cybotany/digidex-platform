from django.http import JsonResponse

from inventory.models import GBIFSpecies


def species_name_suggestion(request):
    query = request.GET.get('q', '')
    if query:
        results = GBIFSpecies.name_suggest(q=query, limit=20)
        suggestions = [
            {'id': result['key'], 'text': result['scientificName']}
            for result in results
        ]
    else:
        suggestions = []
    return JsonResponse({'results': suggestions})