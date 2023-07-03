from django import forms
from django.forms import inlineformset_factory

from apps.botany.models import GrowingMedium, GrowingMediumComponent, GrowingMediumComposition


class GrowingMediumForm(forms.ModelForm):
    class Meta:
        model = GrowingMedium
        fields = ['name', 'description']


GrowingMediumComponentFormSet = inlineformset_factory(
    GrowingMedium,  # parent model
    GrowingMediumComposition,  # inline model
    fields=('component', 'percentage', 'particle_size', 'particle_size_measurement_unit'),  # fields from GrowingMediumComposition
    extra=1,  # number of empty forms to display
    can_delete=True  # ability to delete
)

