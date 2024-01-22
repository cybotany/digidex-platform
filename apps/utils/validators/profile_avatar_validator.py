from django.core.exceptions import ValidationError
from apps.utils.constants import MAX_PROFILE_AVATAR_SIZE, MAX_PROFILE_AVATAR_DIMMENSIONS

def validate_profile_avatar(image):
    # Check file size
    if image.size > MAX_PROFILE_AVATAR_SIZE:
        raise ValidationError('The maximum file size that can be uploaded is 2MB')
    # Check image dimensions
    if image.width > MAX_PROFILE_AVATAR_DIMMENSIONS[0] or image.height > MAX_PROFILE_AVATAR_DIMMENSIONS[1]:
        raise ValidationError(f'The maximum dimensions for the image are {MAX_PROFILE_AVATAR_DIMMENSIONS[0]}x{MAX_PROFILE_AVATAR_DIMMENSIONS[1]} pixels.')
    # Check for square aspect ratio
    if image.width != image.height:
        raise ValidationError('The image must have a 1:1 aspect ratio.')
    # Check for file type
    if image.file.content_type not in ['image/jpeg', 'image/png']:
        raise ValidationError('The file type must be either JPEG or PNG.')
