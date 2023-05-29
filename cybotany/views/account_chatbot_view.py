from django.shortcuts import render
from django.views import View


class AccountChatbotView(View):
    def get(self, request):
        template_name = 'cybotany/chatbot.html'
        return render(request, self.template_name)
