from django.shortcuts import render

from inventory.components import build_top_panel, build_user_navigation

def inventory(request):
    top_panel = build_top_panel(request.user)
    navigation_panel = build_user_navigation(request.user)
    panels = {
        'top_panel': top_panel,
        'navigation_panel': navigation_panel
    }
    template = 'inventory/index.html'
 
    return render(request, template, panels)
