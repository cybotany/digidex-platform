from django.http import JsonResponse

from pygbif import species

def get_species_name_suggestions(query, rank=None, limit=20):
    return species.name_suggest(q=query, rank=rank, limit=limit)

def get_species_backbone(name, kingdom=None, rank=None):
    return species.name_backbone(name=name, kingdom=kingdom, rank=rank)

def species_suggestions_view(request):
    query = request.GET.get('query')
    rank = request.GET.get('rank')
    if not query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)
    suggestions = get_species_name_suggestions(query, rank)
    return JsonResponse(suggestions, safe=False)

def species_backbone_view(request):
    name = request.GET.get('name')
    kingdom = request.GET.get('kingdom')
    rank = request.GET.get('rank')
    if not name:
        return JsonResponse({'error': 'Name parameter is required'}, status=400)
    backbone = get_species_backbone(name, kingdom, rank)
    return JsonResponse(backbone, safe=False)
