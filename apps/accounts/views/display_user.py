from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from apps.accounts.models import Activity


class DisplayUserView(LoginRequiredMixin, View):
    template_name = 'accounts/display_user.html'

    def get(self, request, *args, **kwargs):
        # Fetch the activities related to the user
        recent_activities = Activity.objects.filter(user=request.user).order_by('-timestamp')
        
        # Include the activities in the context
        context = {
            'user': request.user,
            'recent_activities': recent_activities,
        }
        return render(request, self.template_name, context)
