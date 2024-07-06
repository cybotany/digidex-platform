from django.shortcuts import render

from inventory.components import WelcomePanel, CatagoryPanel

def welcome_page(request):
    panels = [
        WelcomePanel(),
        CatagoryPanel(),
    ]

    render(request, 'inventory/index.html', {
        'panels': panels,
    })
