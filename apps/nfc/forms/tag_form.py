from django import forms
from django.contrib.auth import get_user_model
from apps.nfc.models import NFCTag


class NFCTagForm(forms.ModelForm):
    class Meta:
        model = NFCTag
        fields = ['created_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].widget = forms.HiddenInput()
        self.fields['created_by'].initial = get_user_model().objects.get(pk=self.request.user.pk)
