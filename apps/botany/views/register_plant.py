from django.conf import settings
import requests
from django.views import View
from django.shortcuts import render, redirect
from ..models import Plant
from ..forms import PlantRegistrationForm


class RegisterPlant(View):
    template_name = 'botany/new_plant.html'
    model = Plant
    form_class = PlantRegistrationForm
    success_url = '/botany/home'

    def form_valid(self, form):
        plant = form.save(commit=False)
        plant.owner = self.request.user

        identification_id = self.request.session.get('identification_id')

        if identification_id:
            # Fetch the identification result using the identification ID
            headers = {
                "Content-Type": "application/json",
                "Api-Key": settings.PLANT_ID_API_KEY,
            }
            response = requests.get(f"https://api.plant.id/v2/check_identification/{identification_id}", headers=headers).json()

            # Extract information from the response and update the plant object
            # You need to replace this with your actual extraction code
            plant.name = extract_name_from_response(response)

        plant.save()
        return super().form_valid(form)
