from django.shortcuts import render

from inventory.components import build_user_navigation, build_top_panel

def inventory(request):
    top_panel = build_top_panel(request.user)
    navigation_panel = build_user_navigation(request.user)
    panels = [navigation_panel, top_panel]
    template = 'inventory/index.html'
 
    return render(request, template, {'panels': panels})
