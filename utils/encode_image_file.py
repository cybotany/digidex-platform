import base64

def encode_image_file(file):
    """Encode image file to base64."""
    return base64.b64encode(file.read()).decode("ascii")
