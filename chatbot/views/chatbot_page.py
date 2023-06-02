from django.shortcuts import render
from django.views import View


class ChatbotView(View):
    template_name = 'chatbot.html'

    def get(self, request):
        return render(request, self.template_name)
