from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views import View
from apps.chatbot.models import ChatSession


class ChatbotView(LoginRequiredMixin, View):
    template_name = 'chatbot/chat.html'

    def get(self, request):
        # Create a session_id if doesn't exist already
        if not request.session.session_key:
            request.session.create()
            ChatSession.objects.create(
                id=request.session.session_key,
                user=request.user,
                start_time=timezone.now()
            )
        return render(request, self.template_name)
