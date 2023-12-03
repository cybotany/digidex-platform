from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from apps.core.models import Digit
from apps.core.forms import CreateDigitForm
from apps.inventory.models import Link


class DigitizationView(CreateView):
    model = Digit
    form_class = CreateDigitForm
    template_name = 'create_digit.html'

    def form_valid(self, form):
        # Retrieve the link instance using link_id from the URL
        link_id = self.kwargs.get('link_id')
        link = get_object_or_404(Link, id=link_id)

        # Set the link field of the Digit instance
        form.instance.link = link

        # Set the user to the current user
        form.instance.user = self.request.user

        # Update the link instance to be active
        link.active = True
        link.save()

        return super().form_valid(form)
