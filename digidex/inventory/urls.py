from django.urls import path
from digidex.inventory.views import (DetailProfile, UpdateProfile,
                                     CreateGrouping, DetailGrouping,
                                     DetailDigit, UpdateDigit, DeleteDigit)

app_name = 'inventory'
urlpatterns = [
    path('<slug:user_slug>/', DetailProfile.as_view(), name='detail-profile'),
    path('<slug:user_slug>/update/', UpdateProfile.as_view(), name='update-profile'),
    
    path('<slug:user_slug>/add/', CreateGrouping.as_view(), name='add-grouping'),
    path('<slug:user_slug>/<slug:group_slug>/', DetailGrouping.as_view(), name='detail-grouping'),

    path('digit/', DetailDigit.as_view(), name='detail-digit'),
    path('update-digit/', UpdateDigit.as_view(), name='update-digit'),
    path('delete-digit/', DeleteDigit.as_view(), name='delete-digit'),
]
