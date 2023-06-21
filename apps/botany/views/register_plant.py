from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from apps.botany.models import Plant
from apps.botany.forms import PlantRegistrationForm


class RegisterPlantView(View):
    template_name = 'botany/register_plant.html'
    model = Plant
    form_class = PlantRegistrationForm

    def get(self, request, *args, **kwargs):
        form = PlantRegistrationForm(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
            form = PlantRegistrationForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                new_plant = form.save()
                return redirect('botany:upload_plant_image', plant_id=new_plant.id)
            else:
                return render(request, self.template_name, {'form': form})
