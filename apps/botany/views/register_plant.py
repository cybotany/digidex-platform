from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
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
        new_plant = form.save()

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
        kwargs['nfc_tag'] = self.nfc_tag
        return kwargs

    def get(self, request, *args, **kwargs):
        """
        Override the get method to capture the nfc_tag parameter.

        Returns:
            Renders the form with the nfc_tag parameter.
        """
        nfc_tag = request.GET.get('nfc_tag')
        if nfc_tag:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            return self.render_to_response(self.get_context_data(form=form, nfc_tag=nfc_tag))
        else:
            return super().get(request, *args, **kwargs)
