from django.urls import path, include

from accounts.views import profile_form_view

app_name = 'accounts'
urlpatterns = [
    path('inv/', include('inventory.urls')),
    path('<slug:user_slug>/update/', profile_form_view, name='profile_form'),
]
