from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from ..models import Plant
from ..forms import PlantRegistrationForm


class RegisterPlantView(View):
    template_name = 'botany/register_plant.html'
    model = Plant
    form_class = PlantRegistrationForm

    def get(self, request, *args, **kwargs):
        form = PlantRegistrationForm(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PlantRegistrationForm(request.POST)
        if form.is_valid():
            # Store plant details in session and redirect to choose plant form
            request.session['plant_details'] = form.cleaned_data
            return redirect('select_plant')  # assuming the url pattern name for the select plant view is 'select_plant'
        else:
            return render(request, self.template_name, {'form': form})
