from django.views.generic.edit import FormView
from ..forms import PlantSelectionForm
from django.shortcuts import redirect
from django.urls import reverse


class SelectPlantView(FormView):
    template_name = 'botany/select_plant.html'
    form_class = PlantSelectionForm

    def get_form_kwargs(self):
        kwargs = super(SelectPlantView, self).get_form_kwargs()

        # Get the API response
        response = self.request.session.get('api_response', {})

        # update the initial form class
        kwargs.update({
            'choices': response,
        })
        return kwargs

    def form_valid(self, form):
        # Extract chosen plant details from session and API response
        plant_details = self.request.session.get('plant_details', {})
        choice = form.cleaned_data['plant_choice']

        # Store the plant details in the session
        self.request.session['plant_details'] = plant_details

        return redirect(reverse('confirmation'))  # assuming the url pattern name for the confirmation view is 'confirmation'
