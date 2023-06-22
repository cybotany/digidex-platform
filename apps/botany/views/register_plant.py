from django.views.generic import FormView
from django.shortcuts import redirect

from apps.botany.forms import PlantRegistrationForm


class RegisterPlantView(FormView):
    """
    View for registering new plants.
    """
    template_name = 'botany/register_plant.html'
    form_class = PlantRegistrationForm

    def form_valid(self, form):
        new_plant = form.save()
        return redirect('botany:upload_plant_image', pk=new_plant.id)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs