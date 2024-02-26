from django.urls import path
from digidex.inventory.views import (PlantDetails, PlantModification, PlantDeletion,
                                     PetDetails, PetModification, PetDeletion)

app_name = 'inventory'
urlpatterns = [
    path('plant/<uuid:uuid>/', PlantDetails.as_view(), name='plant-details'),
    path('plant/<uuid:uuid>/modification/', PlantModification.as_view(), name='plant-modification'),
    path('plant/<uuid:uuid>/deletion/', PlantDeletion.as_view(), name='plant-deletion'),

    path('pet/<uuid:uuid>/', PetDetails.as_view(), name='pet-details'),
    path('pet/<uuid:uuid>/modification/', PetModification.as_view(), name='pet-modification'),
    path('pet/<uuid:uuid>/deletion/', PetDeletion.as_view(), name='pet-deletion'),
]
