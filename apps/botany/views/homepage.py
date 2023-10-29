from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from apps.botany.models import Plant


class PlantHomepageView(LoginRequiredMixin, TemplateView):
    """
    View for rendering the plant module homepage.
    """
    template_name = 'botany/homepage.html'
    paginate_by = 10

    def get_plants_for_user(self):
        """
        Return all plants for the currently logged-in user.
        """
        plants = Plant.objects.filter(user=self.request.user).order_by('added_on')
        paginator = Paginator(plants, self.paginate_by)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plants'] = self.get_plants_for_user()
        return context
