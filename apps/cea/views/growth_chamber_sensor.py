from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import GrowthChamber, GrowthChamberInstrumentData


class GrowthChamberInstruments(APIView):
    def post(self, request, format=None):
        growth_chamber_id = request.data.get('growth_chamber_id')
        growth_chamber = GrowthChamber.objects.get(id=growth_chamber_id)

        GrowthChamberInstrumentData.objects.create(
            growth_chamber=growth_chamber,
            humidity=request.data.get('humidity'),
            temperature=request.data.get('temperature'),
            pressure=request.data.get('pressure'),
            gas=request.data.get('gas'),
            image_url=request.data.get('image_url'),
        )

        return Response({'detail': 'Sensor data created'}, status=status.HTTP_201_CREATED)
