from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from apps.botany.models import Plant
from apps.botany.forms import PlantImageForm


class UploadPlantImageView(View):
    """
    View for uploading an image for a specific plant.
    """
    template_name = 'botany/upload_plant_image.html'
    form_class = PlantImageForm

    def get(self, request, plant_id):
        plant = self.get_plant(plant_id)
        form = self.form_class()
        return self.render_form(form, plant)

    def post(self, request, plant_id):
        plant = self.get_plant(plant_id)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            self.save_plant_image(form, plant)
            return self.redirect_to_home()
        return self.render_form(form, plant)

    def get_plant(self, plant_id):
        return get_object_or_404(Plant, id=plant_id)

    def save_plant_image(self, form, plant):
        plant_image = form.save(commit=False)
        plant_image.plant = plant
        plant_image.save()

    def render_form(self, form, plant):
        return render(self.request, self.template_name, {'form': form, 'plant': plant})

    def redirect_to_home(self):
        return redirect('botany:home')
