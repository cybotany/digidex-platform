from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

def user_profile(request, slug):
    user = get_object_or_404(User, slug=slug)
    
    if hasattr(user, 'profile_page'):
        return redirect(user.profile_page.url)
    else:
        return render(request, 'inventory/includes/profile/missing.html', {'user': user})
