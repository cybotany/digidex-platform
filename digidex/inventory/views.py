from django.shortcuts import render

from inventory.components import Heading, Category, Item


def index(request):
    template = 'inventory/index.html'
    
    panels = [
        Heading(),
        Category(),
        Item(),
    ]
    context = {'panels': panels}

    return render(request, template, context)
