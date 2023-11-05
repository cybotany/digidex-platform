from apps.itis.models import TaxonomicUnits
from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.models import PlantImage
from apps.botany.forms import PlantRegistrationForm


class RegisterPlantView(FormView):
    """
    View for registering new plants.
    """
    template_name = 'botany/register_plant.html'
    form_class = PlantRegistrationForm

    def form_valid(self, form):
        """
        If the submitted form is valid:
          - Automatically assign the logged on user to the plant.
          - Set a default TSN value if none is provided.
          - Save the plant (Needed before a plant image can be mapped to plant).
          - Save the plant image if one is provided.
          - Log the activity.
          - Redirect the user to the newly created plant detail page
        """
        new_plant = form.save(commit=False)
        new_plant.user = self.request.user

        # Check if TSN value is provided, if not set to plant kingdom tsn (202422)
        if not new_plant.tsn:
            default_taxonomic_unit = TaxonomicUnits.objects.get(tsn=202422)
            new_plant.tsn = default_taxonomic_unit
        else:
            try:
                TaxonomicUnits.objects.get(tsn=new_plant.tsn.tsn)
            except TaxonomicUnits.DoesNotExist:
                # Handle the exception appropriately, e.g., return an error response
                form.add_error('tsn', f"TSN {new_plant.tsn.tsn} does not exist!")
                return self.form_invalid(form)

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
        return redirect(new_plant.get_absolute_url())

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
