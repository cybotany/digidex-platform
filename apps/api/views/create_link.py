from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from apps.inventory.models import Link
from apps.utils.helpers import generate_secret_and_hash

@api_view(['POST'])
def create_link(request):
    # Extract data from request
    serial_number = request.data.get('serial_number')

    # Generate secret and its hash
    secret, secret_hash = generate_secret_and_hash()

    # Create Link instance
    link = Link.objects.create(
        serial_number=serial_number,
        secret_hash=secret_hash
    )

    # Construct the URL with the secret
    url_with_secret = request.build_absolute_uri(reverse('core:link', args=[secret]))

    # Return the URL and status
    return Response({"status": "success", "url": url_with_secret})
