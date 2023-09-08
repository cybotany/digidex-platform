from django import forms
from apps.nfc.models import NFCTag


class NFCTagForm(forms.ModelForm):
    class Meta:
        model = NFCTag
        fields = ['created_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].widget = forms.HiddenInput()