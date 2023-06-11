from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from ..forms import PlantImageForm


class AutoPlantRegistration(FormView):
    template_name = 'botany/auto_plant_registration.html'
    form_class = PlantImageForm
    success_url = reverse_lazy('botany:home')

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        '''
        form.instance.image = self.request.FILES['image']
        return super().form_valid(form)
