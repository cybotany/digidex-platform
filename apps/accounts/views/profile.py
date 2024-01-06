from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from apps.accounts.models import Activity, Profile


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        recent_activities = Activity.objects.filter(user=request.user).order_by('-timestamp')
        user_profile = Profile.objects.get(user=request.user)

        context = {
            'user': request.user,
            'recent_activities': recent_activities,
            'user_profile': user_profile
        }
        return render(request, self.template_name, context)