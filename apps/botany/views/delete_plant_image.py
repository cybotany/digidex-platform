from django.urls import reverse
from django.views.generic.edit import DeleteView
from apps.botany.models import PlantImage


class DeletePlantImageView(DeleteView):
    """
    Deletes a plant image and redirects to the plant description page.
    """
    model = PlantImage
    context_object_name = 'image'
    template_name = 'botany/delete_image.html'

    def get_success_url(self):
        """
        Returns the URL to redirect to after successful deletion.
        """
        return reverse('botany:describe_plant', kwargs={'plant_id': self.object.plant.id})
