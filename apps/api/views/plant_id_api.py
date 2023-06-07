from django.conf import settings
from django.http import JsonResponse
from django.views import View
import requests
import base64
import json


class PlantIdentificationView(View):
    def post(self, request, *args, **kwargs):
        # Ensure the request has an image file
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image provided'}, status=400)
        
        # Read the image file
        image = request.FILES['image'].read()

        # Convert the image file to base64
        encoded_image = base64.b64encode(image).decode('utf-8')

        # Prepare the data for the API request
        data = {
            'organs': ['leaf'],
            'images': [encoded_image]
        }

        # Make the API request
        response = requests.post(
            'https://api.plant.id/v2/identify',
            headers={'Api-Key': settings.PLANT_ID_API_KEY},
            json=data
        )

        # Ensure the API request was successful
        if response.status_code != 200:
            return JsonResponse({'error': 'Plant.id API request failed'}, status=500)

        # Return the API response as JSON
        return JsonResponse(response.json())
