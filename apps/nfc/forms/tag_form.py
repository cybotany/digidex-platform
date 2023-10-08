from django import forms
from django.contrib.auth import get_user_model
from apps.nfc.models import Tag


class NFCTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['serial_number', 'created_by']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if self.request:
            self.fields['created_by'].initial = self.request.user

    def clean_tag_serial_number(self):
        serial_number = self.cleaned_data['serial_number']
        if Tag.objects.filter(serial_number=serial_number, active=True).exists():
            raise forms.ValidationError('This NFC tag is already registered.')
        return serial_number