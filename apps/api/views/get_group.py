from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.groups.models import Group


class GetGroup(APIView):
    permission_classes = [AllowAny]

    def get(self, request, group_id, *args, **kwargs):
        #if not request.user.is_authenticated:
        #    return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch all groups at once and order them.
        user_groups = Group.objects.filter(user=request.user).order_by('position')
        current_group = get_object_or_404(user_groups, id=group_id)

        # Find the current group index. This avoids another query.
        current_group_index = list(user_groups.values_list('id', flat=True)).index(current_group.id)

        # Use modulo for looping effect. 
        prev_group = user_groups[(current_group_index - 1) % len(user_groups)]
        next_group = user_groups[(current_group_index + 1) % len(user_groups)]

        # Prefetch related plants in a single query.
        #plants = Plant.objects.select_related('group').filter(group=current_group)

        # Serialize plants using DRF serializer
        #plant_data = PlantSerializer(plants, many=True).data

        response_data = {
            'current_group_name': current_group.name,
            'prev_group_id': prev_group.id,
            'next_group_id': next_group.id,
            'plants': 0
        }

        return Response(response_data)
