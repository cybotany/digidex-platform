from django.core.exceptions import ValidationError
from digit.utils.constants import MAX_JOURNAL_ENTRY_SIZE, MAX_JOURNAL_ENTRY_DIMMENSIONS

def validate_journal_entry(image):
    # Check file size
    if image.size > MAX_JOURNAL_ENTRY_SIZE:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')
    # Check image dimensions
    if image.width > MAX_JOURNAL_ENTRY_DIMMENSIONS[0] or image.height > MAX_JOURNAL_ENTRY_DIMMENSIONS[1]:
        raise ValidationError(f'The maximum dimensions for the image are {MAX_JOURNAL_ENTRY_DIMMENSIONS[0]}x{MAX_JOURNAL_ENTRY_DIMMENSIONS[1]} pixels.')
    # Check for square aspect ratio
    if image.width != image.height:
        raise ValidationError('The image must have a 1:1 aspect ratio.')
    # Check for file type
    if image.file.content_type not in ['image/jpeg', 'image/png']:
        raise ValidationError('The file type must be either JPEG or PNG.')
