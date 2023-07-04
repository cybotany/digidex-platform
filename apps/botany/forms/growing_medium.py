from django import forms
from django.forms import inlineformset_factory

from apps.botany.models import GrowingMedium, GrowingComponent, GrowingMediumComposition


class GrowingMediumForm(forms.ModelForm):
    class Meta:
        model = GrowingMedium
        fields = ['name', 'description']


GrowingComponentFormSet = inlineformset_factory(
    GrowingMedium,  # parent model
    GrowingMediumComposition,  # inline model
    fields=('growing_component', 'percentage'),
    extra=1,
    can_delete=True
)
