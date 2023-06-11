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
        Here you can handle the uploaded file. For example, you could save it to your model.
        Note that this doesn't save the file to your model, you would need to do that separately.
        You can access the uploaded file with `form.cleaned_data['image']`.
        '''
        return super().form_valid(form)
