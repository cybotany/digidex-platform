import os
import uuid
from django.core.exceptions import ValidationError
from .constants import MEASUREMENT_CHOICES


def calculate_chamber_volume(width, height, length, measurement_system):
    """
    Calculates the volume of a chamber with the given dimensions.

    Args:
        width: The width of the chamber.
        height: The height of the chamber.
        length: The length of the chamber.
        measurement_system: The measurement system to use ('in' for inches, 'cm' for centimeters).

    Returns:
        The volume of the chamber in cubic inches or cubic centimeters, depending on the measurement system.
    """
    volume = width * height * length
    if measurement_system == 'in':
        return volume  # Return volume in cubic inches
    else:
        return volume / 16.387  # Convert cubic inches to cubic centimeters


def get_measurement_system_choice_display(measurement_system):
    """
    Returns the display string for a measurement system choice.

    Args:
        measurement_system: The measurement system choice.

    Returns:
        The display string for the given measurement system choice.
    """
    return next((choice[1] for choice in MEASUREMENT_CHOICES if choice[0] == measurement_system), '')


def validate_file_extension(value):
    """
    Validates that the file extension of the given file is one of the supported extensions.

    Args:
        value: The file to validate.

    Raises:
        ValidationError: If the file extension is not one of the supported extensions.
    """
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file extension. Only {} are supported.'.format(', '.join(valid_extensions)))


def user_directory_path(instance, filename):
    """
    Returns the file path for the given file, based on the owner's ID and a UUID.

    Args:
        instance: The model instance that the file is attached to.
        filename: The original name of the file.

    Returns:
        The file path for the given file.
    """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join(f'owner_{instance.owner.id}', filename)
