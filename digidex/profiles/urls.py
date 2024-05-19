from django.urls import path

from profiles import views

app_name = 'profiles'
urlpatterns = [
    path('<slug:profile_slug>/update/', views.profile_form_view, name='profile_form'),
    path('<slug:profile_slug>/link-ntag/<uuid:ntag_uuid>/', views.create_digit_with_ntag, name='link_ntag'),
]
