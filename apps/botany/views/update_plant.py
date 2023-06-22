from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView

from apps.botany.models import Plant
from apps.botany.forms import PlantImageForm


class UpdatePlantView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for rendering the page used to update plant details.
    """
    model = Plant
    fields = ['name', 'description']
    template_name = 'botany/update_plant.html'
    success_url = reverse_lazy('botany:home')

    def get_context_data(self, **kwargs):
        """
        Returns the context data for rendering the template.

        Returns:
            A dictionary of context data.
        """
        context = super().get_context_data(**kwargs)
        context['image_form'] = self.get_image_form()
        return context

    def get_image_form(self):
        """
        Returns a new instance of the plant image form.

        Returns:
            A new instance of the plant image form.
        """
        return PlantImageForm()

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests. Saves the plant image if valid, then calls the parent post method.

        Args:
            request: The HTTP request.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the parent post method.
        """
        self.object = self.get_object()
        self.handle_image_upload_if_valid(request)
        return super().post(request, *args, **kwargs)

    def handle_image_upload_if_valid(self, request):
        """
        Handles the plant image upload if the form is valid.

        Args:
            request: The HTTP request.
        """
        image_form = PlantImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            self.save_image(image_form)

    def save_image(self, image_form):
        """
        Saves the plant image.

        Args:
            image_form: The valid plant image form.
        """
        image = image_form.save(commit=False)
        image.plant = self.object
        image.save()

    def form_valid(self, form):
        """
        Called when the form is valid. Shows a success message and returns the response from the parent form_valid method.

        Args:
            form: The valid form.

        Returns:
            The response from the parent form_valid method.
        """
        self.show_success_message()
        return super().form_valid(form)

    def show_success_message(self):
        """
        Shows a success message.
        """
        messages.success(self.request, 'Your plant was successfully updated!')

    def test_func(self):
        """
        Returns True if the user is the owner of the plant, False otherwise.

        Returns:
            True if the user is the owner of the plant, False otherwise.
        """
        return self.request.user == self.get_object().owner
