from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from apps.botany.models import Plant
from apps.botany.forms import PlantUpdateForm
from apps.utils.helpers import show_message


class UpdatePlantView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for rendering the page used to update plant details and upload images.
    """
    model = Plant
    form_class = PlantUpdateForm
    template_name = 'botany/update_plant.html'
    success_url = reverse_lazy('botany:home')

    def form_valid(self, form):
        """
        Called when the form is valid. Shows a success message and returns the response from the parent form_valid method.

        Args:
            form: The valid form.

        Returns:
            The response from the parent form_valid method.
        """ 
        self.form.save()      
        show_message(self.request, 'Your plant was successfully updated!', 'success')
        return super().form_valid(form)

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.user
