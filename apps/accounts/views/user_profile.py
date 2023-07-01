from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from apps.accounts.models import Activity


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/user_profile.html'

    def get(self, request, *args, **kwargs):
        recent_activities = Activity.objects.filter(user=request.user).order_by('-timestamp')
        context = {
            'user': request.user,
            'recent_activities': recent_activities,
        }
        return render(request, self.template_name, context)
