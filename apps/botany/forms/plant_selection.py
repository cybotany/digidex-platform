from django import forms


class PlantSelectionForm(forms.Form):
    plant_choice = forms.ChoiceField()

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plant_choice'].choices = choices
