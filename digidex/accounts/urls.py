from django.urls import path

from accounts.views import profile_form_view

urlpatterns = [
    path('<slug:user_slug>/update/', profile_form_view, name='profile_form'),
]
