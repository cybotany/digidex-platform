from django.shortcuts import render
from django.views import View


class AccountChatbotView(View):
    template_name = 'cybotany/chatbot.html'

    def get(self, request):
        return render(request, self.template_name)
