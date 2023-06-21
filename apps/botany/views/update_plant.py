from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from apps.botany.models import Plant
from apps.botany.forms import PlantImageForm


class UpdatePlantView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Plant
    fields = ['name', 'description',]
    template_name = 'botany/update_plant.html'
    success_url = reverse_lazy('botany:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_form'] = PlantImageForm(self.request.POST, self.request.FILES)
        else:
            context['image_form'] = PlantImageForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        image_form = PlantImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.plant = self.object
            image.save()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Your plant was successfully updated!')
        return super().form_valid(form)

    def test_func(self):
        plant = self.get_object()
        return self.request.user == plant.owner
