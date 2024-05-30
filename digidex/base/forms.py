from django import forms


class AssetDeletionCheckbox(forms.Form):
    delete = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'base-radio',
            }
        ),
        required=True
    )
