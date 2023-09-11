from django import forms
from django.contrib.auth import get_user_model
from apps.nfc.models import NFCTag


class NFCTagForm(forms.ModelForm):
    class Meta:
        model = NFCTag
        fields = ['tag_id', 'created_by']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if self.request:
            self.fields['created_by'].initial = self.request.user

    def clean_tag_id(self):
        tag_id = self.cleaned_data['tag_id']
        if NFCTag.objects.filter(tag_id=tag_id, active=True).exists():
            raise forms.ValidationError('This NFC tag is already registered.')
        return tag_id