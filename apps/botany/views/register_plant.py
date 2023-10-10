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
        If the submitted form is valid, save the info to the database and
        redirect the user to the plant detail page.

        Returns:
            Redirects user to the plant detail page of the submitted plant.
        """
        new_plant = form.save(commit=False)
        new_plant.user = self.request.user
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
