from django.db.models import Avg
from .constants import MEASUREMENT_CHOICES


def calculate_chamber_volume(width, height, length, measurement_system):
    volume = width * height * length
    if measurement_system == 'in':
        return volume  # return volume in cubic inches
    else:
        return volume / 16.387  # convert cubic inches to cubic centimeters


def get_measurement_system_choice_display(measurement_system):
    """Return the display string for a measurement system choice."""
    return next((choice[1] for choice in MEASUREMENT_CHOICES if choice[0] == measurement_system), '')


def get_avg_sensor_reading(sensor):
    """Calculate and return the average sensor reading for a given sensor."""
    return sensor.readings.all().aggregate(Avg('value'))['value__avg']


def get_sensor_status(sensor):
    """Return a string indicating the status of a sensor based on its readings."""
    avg_reading = get_avg_sensor_reading(sensor)
    if avg_reading is None:
        return "No readings"
    elif avg_reading < sensor.min_value or avg_reading > sensor.max_value:
        return "Out of range"
    else:
        return "Normal"
