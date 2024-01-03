from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from apps.nfc.models import Link
from django.http import HttpResponse


class LinkingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        uid = request.GET.get('uid')

        if uid:
            try:
                # Decode the ASCII encoded UID
                decoded_uid = bytes.fromhex(uid).decode('ascii')

                # Fetch the Link object based on UID
                try:
                    link = Link.objects.get(uid=decoded_uid)

                    # Redirect to the desired page with the link id
                    return redirect('inventory:digitization', link_id=str(link.id))
                except Link.DoesNotExist:
                    # Handle the case where no Link object is found for the given UID
                    return HttpResponse("Link not found", status=404)
            
            except ValueError:
                # Handle decoding error
                return HttpResponse("Invalid UID format", status=400)
        else:
            return HttpResponse("No UID provided", status=400)
