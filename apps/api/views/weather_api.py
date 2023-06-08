from django.views import View
from django.http import JsonResponse
import requests
from django.conf import settings

api_key = settings.OPEN_WEATHER_MAP_API_KEY


class WeatherView(View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs['label_id']  # Get the label ID from the URL parameters
        location = ""  # Build the location string

        # Send a GET request to the OpenWeatherMap API
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")

        # Parse the JSON response
        data = response.json()

        # You might want to extract specific data from the response, depending on your needs
        # Here's an example of how you might get the current temperature (in Kelvin)
        temperature = data['main']['temp']

        # Return the data as a JSON response
        return JsonResponse({'location': location, 'temperature': temperature})
