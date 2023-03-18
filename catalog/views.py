from django.shortcuts import redirect, render
from catalog.models import Plant


def home_page(request):
    if request.method == 'POST':
        new_plant_entry = request.POST['plant_entry']
        Plant.objects.create(name=new_plant_entry)
        return redirect('/')
    plants = Plant.objects.all()
    return render(request, 'home.html', {'plants': plants})