from django.shortcuts import render

from inventory.components import build_top_panel

def inventory(request):
    content = build_top_panel(request.user)
    context = {'content': content}
    template = 'inventory/index.html'
 
    return render(request, template, context)
