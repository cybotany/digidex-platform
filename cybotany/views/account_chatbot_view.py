from django.shortcuts import render
from django.views import View

class AccountChatbotView(View):
    def get(self, request):
        return render(request, 'cybotany/chatbot.html')
