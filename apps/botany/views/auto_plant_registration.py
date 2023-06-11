from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from ..forms import PlantImageForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AutoPlantRegistration(LoginRequiredMixin, FormView):
    template_name = 'botany/auto_plant_registration.html'
    form_class = PlantImageForm
    success_url = reverse_lazy('botany:home')

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        '''
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)
