from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse

from inventory.models import InventoryTag


def link(request, uuid):
    inventory_tag = get_object_or_404(
        InventoryTag.objects.select_related('link'),
        uuid=uuid
    )
    
    if not inventory_tag.active:
        return HttpResponse("This tag is not active.", status=403)

    return redirect(inventory_tag.link.url)
