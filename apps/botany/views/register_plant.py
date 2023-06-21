from django.views import View
from django.shortcuts import render, redirect

from apps.botany.forms import PlantRegistrationForm


class RegisterPlantView(View):
    """
    View for registering new plants.
    """
    template_name = 'botany/register_plant.html'
    form_class = PlantRegistrationForm

    def get(self, request):
        form = self.form_class(user=request.user)
        return self.render_form(form)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            new_plant = form.save()
            return self.redirect_to_image_upload(new_plant)
        return self.render_form(form)

    def render_form(self, form):
        return render(self.request, self.template_name, {'form': form})

    def redirect_to_image_upload(self, plant):
        return redirect('botany:upload_plant_image', plant_id=plant.id)
