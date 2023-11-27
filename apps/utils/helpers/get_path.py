import os
import uuid

def get_user_directory_path(instance, filename):
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
