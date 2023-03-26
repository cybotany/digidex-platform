from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('cybotany/dashboard')
        else:
            error = 'Invalid username or password'
    else:
        error = ''
    return render(request, 'cybotany/login.html', {'error': error})
