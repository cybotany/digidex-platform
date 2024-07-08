from django.shortcuts import render

from inventory.components import Dashboard

def index(request):
    content = Dashboard.from_user(request.user)
    context = {'content': content}
    template = 'inventory/index.html'
 
    return render(request, template, context)
