from django.views.generic.edit import FormMixin
from django.views.generic import DetailView
from apps.botany.forms import PlantForm
from apps.botany.models import Plant
from apps.utils.helpers import show_message


class PlantView(FormMixin, DetailView):
    """
    View for rendering the page used to show details about a specific registered plant.
    """
    model = Plant
    template_name = 'botany/describe_plant.html'
    form_class = PlantForm
    context_object_name = 'plant'

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.get_form()
        context['watering_events'] = self.object.waterings.all().order_by('-timestamp')
        context['fertilization_events'] = self.object.fertilizations.all().order_by('-timestamp')
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        plant_name = self.object.name
        success_message = f'"{plant_name}" was successfully updated!'
        show_message(self.request, success_message, 'success')
        return super().form_valid(form)

