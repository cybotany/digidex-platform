from django.views.generic import FormView
from django.shortcuts import get_object_or_404

from apps.botany.models import Plant
from apps.botany.forms import PlantImageForm


class UploadPlantImageView(FormView):
    """
    View for uploading images for a plant.
    """
    template_name = 'botany/upload_plant_image.html'
    form_class = PlantImageForm

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.

        Returns:
            A dictionary of keyword arguments.
        """
        kwargs = super().get_form_kwargs()
        kwargs['plant'] = self.get_plant()
        return kwargs

    def get_plant(self):
        """
        Returns the plant object.

        Returns:
            The plant object.
        """
        return get_object_or_404(Plant, id=self.kwargs['pk'])

    def form_valid(self, form):
        """
        Called when the form is valid. Saves the new plant image.

        Args:
            form: The valid form.

        Returns:
            The response from the parent form_valid method.
        """
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful form submission.

        Returns:
            The URL to redirect to after a successful form submission.
        """
        return self.get_plant().get_absolute_url()