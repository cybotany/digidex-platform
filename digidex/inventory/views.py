from django.shortcuts import render

from inventory.components import HeadingSection

def index(request):
    content = HeadingSection.from_user(request.user)
    context = {'content': content}
    template = 'inventory/index.html'
 
    return render(request, template, context)
