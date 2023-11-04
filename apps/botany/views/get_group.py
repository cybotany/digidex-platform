from django.http import JsonResponse
from django.views import View
from apps.botany.models import Plant


class GetPlantsByGroupView(View):
    def get(self, request, group_id, *args, **kwargs):
        plants = Plant.objects.filter(group_id=group_id).values('id', 'name', 'description')
        return JsonResponse(list(plants), safe=False)
