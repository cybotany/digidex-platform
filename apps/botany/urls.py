from django.urls import path
from apps.botany.views import (
    RegisterPlantView,
    DescribePlantView,
    DeletePlantView,
)


app_name = 'botany'
urlpatterns = [
    path('register/plant/', RegisterPlantView.as_view(), name='register_plant'),
    path('plant/<int:pk>/describe/', DescribePlantView.as_view(), name='describe_plant'),
    path('plant/<int:pk>/delete/', DeletePlantView.as_view(), name='delete_plant'),
]
