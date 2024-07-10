from django.shortcuts import render

from inventory.components import DashboardComponent

def inventory(request):
    template = 'inventory/index.html'
    context = {
        'dashboard': DashboardComponent(request.user)
    }
 
    return render(
        request,
        template,
        context
    )
