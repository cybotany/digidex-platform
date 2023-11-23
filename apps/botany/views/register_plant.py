from django.views.generic import FormView
from django.shortcuts import redirect, get_object_or_404
from apps.accounts.models import Activity
from apps.botany.forms import PlantRegistrationForm
from apps.nfc.models import Tag
from apps.utils.helpers import show_message

class RegisterPlantView(FormView):
    """
    View for registering new plants.
    """
    template_name = 'botany/register_plant.html'
    form_class = PlantRegistrationForm

    def form_valid(self, form):
        new_plant = form.save()

        # Associate NFC tag with the plant
        nfc_tag_sn = self.request.session.pop('nfc_tag_sn', None)
        if nfc_tag_sn:
            tag = get_object_or_404(Tag, serial_number=nfc_tag_sn, created_by=self.request.user)
            tag.plant = new_plant
            tag.save()

        Activity.objects.create(
            user=self.request.user,
            activity_status='register',
            activity_type='plant',
            content=f'Registered a new plant: {new_plant.name}',
        )

        success_message = f'"{new_plant.name}" was successfully registered!'
        show_message(self.request, success_message, 'success')
        return redirect(new_plant.get_absolute_url())

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the PlantRegistrationForm
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
