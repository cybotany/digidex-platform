from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventory.models import InventoryPage

class InventoryPageAssetSectionView(APIView):
    def get(self, request, uuid):
        try:
            page = InventoryPage.objects.get(uuid=uuid)
            asset_section = page.get_asset_section()
            return Response(asset_section, status=status.HTTP_200_OK)
        except InventoryPage.DoesNotExist:
            return Response({"error": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
