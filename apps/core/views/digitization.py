from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from apps.core.models import Digit
from apps.core.forms import CreateDigitForm


class DigitizationView(CreateView):
    model = Digit
    form_class = CreateDigitForm
    template_name = 'create_digit.html'
    success_url = reverse_lazy('digit-list')

    def form_valid(self, form):
        # Set the user to the current user
        form.instance.user = self.request.user
        return super().form_valid(form)
