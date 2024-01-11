import os
import uuid
from datetime import datetime

def get_unique_filename(instance, filename):
    """
    Generates a unique filename using a combination of the instance's ID,
    user's ID, and a unique identifier.

    Args:
        instance: The model instance (Profile or Entry).
        filename: The original filename of the image.

    Returns:
        A unique filename.
    """
    ext = os.path.splitext(filename)[1]
    # Use the current timestamp as a unique identifier
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    # Profile instance
    if hasattr(instance, 'user'):
        return f'{instance._meta.model_name}/{instance.user.id}/image-{timestamp}{ext}'
    # Entry instance
    elif hasattr(instance, 'digit'):
        return f'{instance._meta.model_name}/{instance.digit.id}/image-{timestamp}{ext}'
    else:
        # Default format
        return f'uploads/image-{uuid.uuid4()}{ext}'

def get_user_directory_path(instance, filename):
    """
    Generates a unique filename using a combination of the instance's ID,
    user's ID, and a unique identifier.

    Args:
        instance: The model instance (Profile or Entry).
        filename: The original filename of the image.

    Returns:
        A unique filename.
    """
    ext = os.path.splitext(filename)[1]
    # Use the current timestamp as a unique identifier
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    # Profile instance
    if hasattr(instance, 'user'):
        return f'{instance._meta.model_name}/{instance.user.id}/image-{timestamp}{ext}'
    # Entry instance
    elif hasattr(instance, 'digit'):
        return f'{instance._meta.model_name}/{instance.digit.id}/image-{timestamp}{ext}'
    else:
        # Default format
        return f'uploads/image-{uuid.uuid4()}{ext}'
