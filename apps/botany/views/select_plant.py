from django.shortcuts import render
from .forms import ChoosePlantForm


def choose_plant(request):
    if request.method == 'POST':
        form = ChoosePlantForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            plant_details = extract_plant_details_for_choice(response, choice)
            form = PlantRegistrationForm(initial=plant_details)
            return render(request, 'plant_registration.html', {'form': form})
    else:
        response = ...  # Get the API response
        form = ChoosePlantForm(initial={'choices': extract_choices(response)})
    return render(request, 'choose_plant.html', {'form': form})
