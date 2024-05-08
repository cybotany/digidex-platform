from django.urls import path

from profiles import views

app_name = 'profiles'
urlpatterns = [
    path('<slug:user_slug>/update/', views.profile_form_view, name='profile_form'),
]
