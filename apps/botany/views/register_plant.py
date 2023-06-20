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
        form = PlantRegistrationForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('botany:home')
        else:
            return render(request, self.template_name, {'form': form})
