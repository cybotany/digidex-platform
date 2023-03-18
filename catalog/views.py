from django.shortcuts import render
from catalog.models import Plant


def home_page(request):
    if request.method == 'POST':
        new_plant_entry = request.POST['plant_entry']
        Plant.objects.create(name=new_plant_entry)
    else:
        new_plant_entry = ''

    #plant = Plant()
    #plant.name = request.POST.get('plant_entry', '')
    #plant.save()

    return render(request, 'home.html', {'new_plant_entry': new_plant_entry,})