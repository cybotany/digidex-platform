from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import GrowthChamber, Sensor, Instrument


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'type', 'description', 'location', 'min_value', 'max_value', 'value_unit']



class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['name', 'type', 'description', 'location']


class GrowthChamberForm(forms.ModelForm):
    class Meta:
        model = GrowthChamber
        fields = ('name', 'description', 'location', 'measurement_system', 'chamber_width', 'chamber_height', 'chamber_length', 'sensors', 'instruments')
