from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(
        request,
        'home.html',
        {'new_plant_entry': request.POST.get('plant_entry', ''), }
    )
