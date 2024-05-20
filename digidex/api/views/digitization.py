from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from digitization.models import UserDigit
from api.serializers.digitization import UserDigitSerializer


class UserDigitListView(generics.ListAPIView):
    serializer_class = UserDigitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = self.kwargs['category']
        user = self.request.user
        if category == 'party':
            return UserDigit.objects.filter(party__user=user)
        return UserDigit.objects.filter(inventory_group__name=category, inventory_group__user=user)
