from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class ChatbotView(LoginRequiredMixin, View):
    template_name = 'chatbot/chat.html'

    def get(self, request):
        return render(request, self.template_name)
