from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.forms import UserProfileForm

@login_required
def update_user_profile_view(request):
    user = request.user
    profile = user.get_profile()
    page = profile.get_page()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = user
            new_profile.save()
            return redirect('page')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/user_profile_form.html', {'form': form})
