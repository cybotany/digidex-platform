from django.core.exceptions import ValidationError


def validate_image_size_and_dimensions(image):
    max_size = 1024 * 1024  # 1MB
    max_width = 256
    max_height = 256

    if image.size > max_size:
        raise ValidationError('The maximum file size that can be uploaded is 1MB')

    if image.width > max_width or image.height > max_height:
        raise ValidationError('The maximum dimensions for the image are 256x256')
