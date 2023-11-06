from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.botany.models import Plant, Group
from apps.api.serializers import PlantSerializer


class GetPlantGroup(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, group_id, *args, **kwargs):
        # User's authentication credentials aren't provided
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        current_group = get_object_or_404(Group, id=group_id, user=request.user)
        user_groups = list(Group.objects.filter(user=request.user).order_by('position'))

        # Find the current group index.
        current_group_index = user_groups.index(current_group)

        # Use modulo for looping effect. 
        prev_group = user_groups[(current_group_index - 1) % len(user_groups)]
        next_group = user_groups[(current_group_index + 1) % len(user_groups)]

        plants = Plant.objects.filter(user=request.user, group=current_group)

        # Serialize plants using DRF serializer
        plant_data = PlantSerializer(plants, many=True).data

        response_data = {
            'current_group_name': current_group.name,
            'prev_group_id': prev_group.id,
            'next_group_id': next_group.id,
            'plants': plant_data
        }

        return Response(response_data)
