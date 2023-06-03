from django.shortcuts import render
from django.views import View


class Chat(View):
    template_name = 'chatbot/chat.html'

    def get(self, request):
        return render(request, self.template_name)
