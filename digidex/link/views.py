from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.template.response import TemplateResponse

from link.models import InventoryTag


def link(request):
    uuid = request.GET.get("uuid", None)
    if uuid:
        inventory_tag = get_object_or_404(
            InventoryTag.objects.select_related('link', 'link__inventory'),
            uuid=uuid
        )
        if not inventory_tag.active:
            return HttpResponse("This tag is not active.", status=403)
        
        try:            
            ntag_link = inventory_tag.link
            return redirect(ntag_link.inventory.url)

        except ValidationError as e:
            return HttpResponse(str(e), status=400)
    else:
        return TemplateResponse(
            request,
            "link/link.html",
        )
