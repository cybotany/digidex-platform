from django.shortcuts import render

from inventory.components import HeadingPanel, CategoryPanel, ItemPanel


def index(request):
    template = 'inventory/index.html'
    
    panels = [
        HeadingPanel(),
        CategoryPanel(),
        ItemPanel(),
    ]
    context = {'panels': panels}

    return render(request, template, context)
