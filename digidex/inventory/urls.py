from django.urls import path
from digidex.inventory.views import (DetailPet, UpdatePet, DeletePet,
                                     DetailPlant, UpdatePlant, DeletePlant)

app_name = 'inventory'
urlpatterns = [
    path('pet/<uuid:uuid>/', DetailPet.as_view(), name='detail-pet'),
    path('pet/<uuid:uuid>/update/', UpdatePet.as_view(), name='update-pet'),
    path('pet/<uuid:uuid>/delete/', DeletePet.as_view(), name='delete-pet'),

    path('plant/<uuid:uuid>/', DetailPlant.as_view(), name='detail-plant'),
    path('plant/<uuid:uuid>/update/', UpdatePlant.as_view(), name='update-plant'),
    path('plant/<uuid:uuid>/delete/', DeletePlant.as_view(), name='delete-plant'),
]
