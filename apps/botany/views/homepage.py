from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from apps.botany.models import Group, Plant
from apps.utils.helpers import is_ajax


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'botany/homepage.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the total number of groups the user has
        user_groups = Group.objects.filter(user=self.request.user)
        total_groups = user_groups.count()

        # Paginate the groups
        paginator = Paginator(range(1, total_groups + 1), self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        # Fetch plants for the group matching the page number
        group_id = page_obj.number
        current_group = user_groups.filter(position=group_id)
        plants_in_group = Plant.objects.filter(user=self.request.user, group_id=current_group.id)

        context['page_obj'] = page_obj
        context['plants'] = plants_in_group
        context['group'] = current_group
        return context


    def get(self, request, *args, **kwargs):
        if is_ajax(request):
            context = self.get_context_data(**kwargs)
            html = render_to_string('botany/partials/group_list.html', context, request=request)
            return JsonResponse({'html': html})
        else:
            return super().get(request, *args, **kwargs)
