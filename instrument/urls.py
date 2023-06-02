from django.urls import path
from instrument.views import SensorSetupView


urlpatterns = [
    path('sensor-setup/', SensorSetupView.as_view(), name='sensor_setup'),
]
