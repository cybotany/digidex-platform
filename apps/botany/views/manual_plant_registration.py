from django.views.generic import TemplateView


class ManualPlantRegistration(TemplateView):
    template_name = 'botany/manual_plant_registration.html'
