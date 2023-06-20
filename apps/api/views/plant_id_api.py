from django.views.generic.edit import FormView
from django.conf import settings
import requests
import time
from django.shortcuts import redirect
from django.urls import reverse
from apps.utils.helpers import encode_image_file
from apps.botany.forms import PlantIdentificationForm, PlantRegistrationForm


class PlantIdentificationAPIView(FormView):
    template_name = 'api/identify_plant.html'
    form_class = PlantIdentificationForm

    def form_valid(self, form):
        image = form.cleaned_data.get('image')
        encoded_image = encode_image_file(image)

        current_datetime = int(time.time())

        params = {
            "images": [encoded_image],
            "datetime": current_datetime,
            "modifiers": ["crops_fast", "similar_images"],
            "plant_details": ["common_names",
                              "edible_parts",
                              "gbif_id",
                              "name_authority",
                              "propagation_methods",
                              "synonyms",
                              "taxonomy",
                              "url",
                              "wiki_description",
                              "wiki_image",
                              ],
        }

        headers = {
            "Content-Type": "application/json",
            "Api-Key": settings.PLANT_ID_API_KEY,
        }

        response = requests.post("https://api.plant.id/v2/enqueue_identification",
                                 json=params,
                                 headers=headers).json()

        self.request.session['identification_id'] = response["id"]
        return redirect(reverse('botany:register_plant'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlantRegistrationForm(user=self.request.user)
        return context
