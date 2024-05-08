from django.urls import path

from profiles import views

app_name = 'profiles'
urlpatterns = [
    path('<slug:user_slug>/update/', views.update_user_profile_view, name='update_user_profile'),
]
