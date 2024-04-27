from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User

def user_profile(request, slug):
    user = get_object_or_404(User, slug=slug)
    
    if hasattr(user, 'user_profile_page'):
        return redirect(user.user_profile_page.url)
    else:
        return render(request, 'inventory/missing_profile.html', {'user': user})
