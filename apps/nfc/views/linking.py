from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from apps.nfc.models import Link
from django.http import HttpResponse


class LinkingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        mirrored_data = request.GET.get('data')

        if mirrored_data:
            try:
                # Decode the ASCII encoded string
                decoded_data = bytes.fromhex(mirrored_data).decode('ascii')

                # Split the UID and counter values
                uid, counter_str = decoded_data.split('x')
                counter = int(counter_str)

                # Fetch the Link object based on UID
                try:
                    link = Link.objects.get(uid=uid)
                    # Update the counter field
                    link.counter = counter
                    link.save()

                    # Redirect to the desired page with the link id
                    #return redirect('inventory:digitization', link_id=str(link.id))
                    return HttpResponse("Link has been found found!", status=404)
                except Link.DoesNotExist:
                    # Handle the case where no Link object is found for the given UID
                    return HttpResponse("Link not found", status=404)
            
            except ValueError:
                # Handle decoding error or split error
                return HttpResponse("Invalid data format", status=400)
        else:
            return HttpResponse("No data provided", status=400)
