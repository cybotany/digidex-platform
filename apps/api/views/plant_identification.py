from django.views.generic.edit import FormView
from django.conf import settings
import requests
from apps.utils.helpers import encode_image_file, process_location
from ..forms import PlantIdentificationForm


class PlantIdentification(FormView):
    template_name = 'identify_plant.html'
    form_class = PlantIdentificationForm
    success_url = '/botany/identify-plant'

    def form_valid(self, form):
        location = form.cleaned_data.get('location')
        images = form.cleaned_data.get('images')
        encoded_images = [encode_image_file(img) for img in images]

        latitude, longitude = process_location(location)
        params = {
            "images": encoded_images,
            "latitude": latitude,
            "longitude": longitude,
            "datetime": 1582830233,
            "modifiers": ["crops_fast", "similar_images"],
        }

        headers = {
            "Content-Type": "application/json",
            "Api-Key": settings.PLANT_ID_API_KEY,
        }

        response = requests.post("https://api.plant.id/v2/enqueue_identification",
                                json=params,
                                headers=headers).json()
        
        # Store the ID in the session so it can be accessed in the result view
        self.request.session['identification_id'] = response["id"]
        return super().form_valid(form)
