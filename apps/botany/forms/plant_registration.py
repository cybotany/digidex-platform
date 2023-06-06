from django import forms
from ..models import Plant, Label


class PlantRegistrationForm(forms.ModelForm):
    label = forms.ModelChoiceField(queryset=Label.objects.none(), required=False)

    class Meta:
        model = Plant
        fields = ('name', 'label',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # To populate the label field with the current user's labels
        self.fields['label'].queryset = Label.objects.filter(user=self.user)

    def save(self, commit=True):
        plant = super().save(commit=False)
        plant.owner = self.user
        if commit:
            plant.save()
        return plant
