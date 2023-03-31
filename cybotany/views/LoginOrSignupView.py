from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

def login_or_signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log the user in and redirect to the dashboard
            login(request, user)
            return redirect("dashboard")

        else:
            # Check if the email exists in the database
            if User.objects.filter(email=email).exists():
                # Email exists, but the password is incorrect
                return HttpResponse("Incorrect password. Please try again.")
            else:
                # Email not found, redirect to the signup info page
                return redirect("signup_info")

    else:
        # Render the homepage with the login/signup form
        return render(request, "index.html")
