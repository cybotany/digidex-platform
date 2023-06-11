from django import forms


class PlantImageForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput)
