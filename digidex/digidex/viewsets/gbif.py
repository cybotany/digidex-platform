from django.shortcuts import render
from django.http import JsonResponse

from serializers.gbif import get_species_name_suggestions, get_species_backbone

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
