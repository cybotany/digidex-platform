# views.py
from django.views.generic.list import ListView
from apps.inventory.models import Group

class GroupingView(ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'groups'
    paginate_by = 1

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user).order_by('name')
