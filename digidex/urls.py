"""
digidex URL Configuration
"""
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('digidex.main.urls')),
    path('user/', include('digidex.accounts.urls')),
    path('api/', include('digidex.api.urls')),
    path('link/', include('digidex.link.urls')),
    path('digit', include('digidex.inventory.urls')),
    path('', include('digidex.journal.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]