from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from apps.botany.models import Plant, Group
from django.core import serializers


class GetGroupView(View):
    def get(self, request, group_id, *args, **kwargs):
        current_group = get_object_or_404(Group, id=group_id, user=request.user)
        user_groups = list(Group.objects.filter(user=request.user).order_by('position'))

        # Find the current group index.
        current_group_index = user_groups.index(current_group)
        
        # Use modulo for looping effect. 
        prev_group = user_groups[(current_group_index - 1) % len(user_groups)]
        next_group = user_groups[(current_group_index + 1) % len(user_groups)]

        plants = Plant.objects.filter(user=request.user, group=current_group)

        # Serialize plants to JSON
        plant_data = serializers.serialize('json', plants)
        response_data = {
            'current_group_name': current_group.name,
            'prev_group_id': prev_group.id,
            'next_group_id': next_group.id,
            'plants': plant_data
        }

        return JsonResponse(response_data, safe=False)
