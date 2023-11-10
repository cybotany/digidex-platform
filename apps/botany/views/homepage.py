from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from apps.botany.models import Group
from apps.utils.constants import MAX_GROUP
from apps.utils.helpers import is_ajax


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'botany/homepage.html'
    paginate_by = MAX_GROUP

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_groups = Group.objects.filter(user=self.request.user).order_by('position')
        user_groups = list(user_groups)

        paginator = Paginator(user_groups, 1)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context


    def get(self, request, *args, **kwargs):
        if is_ajax(request):
            context = self.get_context_data(**kwargs)
            html = render_to_string('botany/partials/group_list.html', context, request=request)
            return JsonResponse({'html': html})
        else:
            return super().get(request, *args, **kwargs)
