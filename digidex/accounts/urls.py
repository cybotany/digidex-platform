from django.urls import path, include

from accounts.views import update_account_view, delete_account_view

app_name = 'accounts'
urlpatterns = [
    path('inv/', include('inventory.urls')),
    path('<slug:user_slug>/update/', update_account_view, name='update_account'),
    path('<slug:user_slug>/delete/', delete_account_view, name='delete_account'),
]
