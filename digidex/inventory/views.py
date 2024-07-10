from django.shortcuts import render

from inventory.components import build_user_navigation, build_top_panel

def inventory(request):
    template = 'inventory/index.html'
    top_panel = build_top_panel(request.user)
    navigation_panel = build_user_navigation(request.user)
    context = {
        'panels': [
            navigation_panel,
            top_panel
        ]
    }
 
    return render(
        request,
        template,
        context
    )
