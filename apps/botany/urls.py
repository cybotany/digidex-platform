from django.urls import path
from .views import CreateLabelView, DescribePlantView, DeletePlantView, EditPlantView, PlantHomepageView, RegisterPlantView, SelectPlantView


app_name = 'botany'
urlpatterns = [
    path('', PlantHomepageView.as_view(), name='home'),
    path('create-label', CreateLabelView.as_view(), name='create_label'),
    path('register-plant', RegisterPlantView.as_view(), name='register_plant'),
    path('select-plant', SelectPlantView.as_view(), name='select_plant'),
    path('plants/<int:pk>/describe', DescribePlantView.as_view(), name='describe_plant'),
    path('plants/<int:pk>/edit', EditPlantView.as_view(), name='edit_plant'),
    path('plants/<int:pk>/delete', DeletePlantView.as_view(), name='delete_plant'),
]
