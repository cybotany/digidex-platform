from django.shortcuts import redirect, render
from django.http import HttpResponse
from catalog.models import Plant


def home_page(request):
    if request.method == 'POST':
        Plant.objects.create(name=request.POST['plant_entry'])
        return redirect('/')
    return render(request, 'home.html')
