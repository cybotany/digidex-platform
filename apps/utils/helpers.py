import os
import base64
import uuid
import re

from apps.utils.constants import MEASUREMENT_CHOICES


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


def encode_image_file(file):
    """Encode image file to base64."""
    return base64.b64encode(file.read()).decode("ascii")


def parse_and_export_sql_file(filename):
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        content = file.read()

    # Split content based on the provided pattern
    segments = re.split(r'-- Data for Name: (\w+); Type: TABLE DATA; Schema: public; Owner: -', content)

    # Iterate over segments in pairs (entity name and SQL content)
    for idx in range(1, len(segments), 2):
        entity_name = segments[idx]
        sql_content = segments[idx + 1]

        output_filename = f"/home/raphael/ITIS_{entity_name}.sql"

        with open(output_filename, 'w', encoding='ISO-8859-1') as output_file:
            output_file.write(f"-- Data for Name: {entity_name}; Type: TABLE DATA; Schema: public; Owner: -\n")
            output_file.write(sql_content)

    print(f"Exported {len(segments) // 2} SQL files.")
