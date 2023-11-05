from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from apps.botany.models import Plant, Group


class GetGroupView(View):
    def get(self, request, group_id, *args, **kwargs):
        group = get_object_or_404(
            Group,
            id=group_id,
            user=request.user
        )

        plants = Plant.objects.filter(
            user=request.user,
            group=group
        ).values('id', 'name', 'description')

        return JsonResponse(list(plants), safe=False)
