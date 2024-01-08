from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from apps.inventory.forms import DigitForm
from apps.inventory.models import Digit


class DigitModificationView(UpdateView):
    model = Digit
    form_class = DigitForm
    template_name = 'inventory/digit_modification.html'

    def get_object(self, queryset=None):
        digit_id = self.kwargs.get('pk')
        return get_object_or_404(Digit, pk=digit_id)

    def form_valid(self, form):
        # Save the form and then redirect
        form.save()
        return redirect('inventory:details', pk=self.object.pk)
