from django.forms import Media
from django.shortcuts import render

from inventory.components import WelcomePanel

def welcome_page(request):
    panels = [
        WelcomePanel(),
    ]

    media = Media()
    for panel in panels:
        media += panel.media

    render(request, 'inventory/welcome.html', {
        'panels': panels,
        'media': media,
    })
