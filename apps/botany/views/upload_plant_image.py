from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from apps.botany.models import Plant
from apps.botany.forms import PlantImageForm


class UploadPlantImageView(View):
    template_name = 'botany/upload_plant_image.html'

    def get(self, request, *args, **kwargs):
        plant_id = kwargs['plant_id']
        plant = get_object_or_404(Plant, id=plant_id)
        form = PlantImageForm()
        return render(request, self.template_name, {'form': form, 'plant': plant})

    def post(self, request, *args, **kwargs):
        plant_id = kwargs['plant_id']
        plant = get_object_or_404(Plant, id=plant_id)
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save(commit=False)
            plant_image.plant = plant
            plant_image.save()
            return redirect('botany:home')
        else:
            return render(request, self.template_name, {'form': form, 'plant': plant})
