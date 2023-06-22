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
        # Save the plant and associated images
        new_plant = form.save()
        return redirect(new_plant.get_absolute_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Add the user to the form kwargs
        kwargs['user'] = self.request.user
        return kwargs
