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
        """
        Called when the form is valid. Saves the new plant and redirects to the image upload page.

        Args:
            form: The valid form.

        Returns:
            A redirect to the image upload page for the new plant.
        """
        new_plant = form.save()
        return redirect('botany:upload_plant_image', pk=new_plant.id)
