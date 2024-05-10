from django.urls import path, include

from profiles import views

app_name = 'profiles'
urlpatterns = [
    path('<slug:profile_slug>/update/', views.profile_form_view, name='profile_form'),
    path('<slug:profile_slug>/inventory/', include('inventory.urls')),
]
