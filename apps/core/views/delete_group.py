from django.views import View
from django.shortcuts import get_object_or_404, redirect
from apps.inventory.models import Group
from apps.core.models import Digit


class DeleteGroupView(View):
    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        if Digit.objects.filter(group=group).exists():
            return redirect('core:group-detail', pk=pk)
        group.delete()
        return redirect('core:garden')
