from django import forms
from apps.botany.models import Plant, Label


class PlantRegistrationForm(forms.ModelForm):
    label = forms.ModelChoiceField(queryset=Label.objects.none(), required=False)

    class Meta:
        model = Plant
        fields = ('name',
                  'label',
                  'common_names',
                  'description',
                  'edible_parts',
                  'gbif_species_id',
                  'propagation_methods',
                  'scientific_name',
                  'synonyms',
                  'taxonomy',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        user_labels = Label.objects.filter(user=self.user)
        common_labels = Label.get_common_labels()
        self.fields['label'].queryset = user_labels | common_labels

    def save(self, commit=True):
        plant = super().save(commit=False)
        plant.owner = self.user
        if commit:
            plant.save()
        return plant
