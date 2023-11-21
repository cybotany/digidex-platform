from apps.itis.models import TaxonomicUnits
from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.models import PlantImage
from apps.botany.forms import PlantRegistrationForm
from apps.utils.helpers import show_message


class RegisterPlantView(FormView):
    """
    View for registering new plants.
    """
    template_name = 'botany/register_plant.html'
    form_class = PlantRegistrationForm

    def form_valid(self, form):
        new_plant = form.save(commit=False)
        new_plant.user = self.request.user

        # Check if TSN value is provided, if not set to plant kingdom tsn (202422)
        if not new_plant.tsn:
            default_taxonomic_unit = TaxonomicUnits.objects.get(tsn=202422)
            new_plant.tsn = default_taxonomic_unit.tsn
        else:
            try:
                TaxonomicUnits.objects.get(tsn=new_plant.tsn.tsn)
            except TaxonomicUnits.DoesNotExist:
                # Handle the exception appropriately, e.g., return an error response
                form.add_error('tsn', f"TSN {new_plant.tsn.tsn} does not exist!")
                return self.form_invalid(form)

        group = form.cleaned_data.get('group')
        if group:
            new_plant.group = group

        new_plant.save()

        image = form.cleaned_data.get('image')
        if image:
            PlantImage.objects.create(plant=new_plant, image=image)

        Activity.objects.create(
            user=self.request.user,
            activity_status='register',
            activity_type='plant',
            content=f'Registered a new plant: {new_plant.name}',
        )

        success_message = f'"{new_plant.name}" was successfully registered!'
        show_message(self.request, success_message, 'success')
        return redirect(new_plant.get_group_url())

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the PlantRegistrationForm

        Returns:
            kwargs dictionary with the key 'user' assigned to value self.request.user
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        nfc_tag = self.request.session.pop('nfc_tag', None)
        if nfc_tag:
            kwargs['nfc_tag'] = nfc_tag
        return kwargs
