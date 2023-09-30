import os
import base64
import uuid

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


def convert_copy_to_insert(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Find the start and end of the COPY block
    start = None
    end = None
    for i, line in enumerate(lines):
        if line.startswith("COPY"):
            start = i
        if line.startswith("\\."):
            end = i
            break

    if start is None or end is None:
        print("No valid COPY block found.")
        return

    # Extract column names from the COPY command
    columns_line = lines[start].split("(")[1].split(")")[0]
    columns = [col.strip() for col in columns_line.split(",")]

    # Process each data line
    insert_statements = []
    for line in lines[start + 1:end]:
        values = line.split("\t")
        # Replace \N with NULL
        values = ['NULL' if val == '\\N' else f"'{val.strip()}'" for val in values]
        insert_statements.append(f"INSERT INTO itis_taxonomicunits ({', '.join(columns)}) VALUES ({', '.join(values)});")

    # Replace the COPY block with the INSERT statements
    output = lines[:start] + insert_statements + lines[end + 1:]

    # Write the result to a new file
    with open("output.sql", 'w') as file:
        file.writelines(output)

    print("Conversion completed. Check output.sql.")

if __name__ == "__main__":
    convert_copy_to_insert("input.sql")
