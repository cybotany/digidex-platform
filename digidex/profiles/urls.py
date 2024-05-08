from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('<uuid:ntag_uuid>/link/ntag/', views.update_user_profile_view, name='update_profile'),
]
