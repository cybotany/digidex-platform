from django.shortcuts import render, get_object_or_404, redirect

from accounts import models

def user_profile(request, slug):
    user = get_object_or_404(models.User, slug=slug)
    
    if hasattr(user, 'profile_page'):
        return redirect(user.profile_page.url)
    else:
        return render(request, 'accounts/missing_profile.html', {'user': user})
