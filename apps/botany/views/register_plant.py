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
        If the submitted form is valid, save the info to the database and
        redirect the user to the plant detail page.
        """
        new_plant = form.save()
        return redirect(new_plant.get_absolute_url())

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the PlantRegistrationForm

        Returns:
            kwargs dictionary with the key 'user' assigned to value self.request.user
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
