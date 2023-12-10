from django.views import View
from django.shortcuts import get_object_or_404, redirect
from apps.inventory.models import Group


class DeleteGroupView(View):
    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return redirect('core:garden')
