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

        nfc_uuid = self.request.session.pop('nfc_uuid', None)
        if nfc_uuid:
            tag = get_object_or_404(Tag, uuid=nfc_uuid)
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
