from django import forms

from inventory.models import UserDigitizedObject, UserDigitizedObjectJournal


class UserDigitizedObjectForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Enter the name of the digitized object'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'text-field textarea',
                'placeholder': 'Provide a detailed description of the object'
            }
        )
    )

    def save(self, user_profile, commit=True):
        digitized_object = UserDigitizedObject(
            user_profile=user_profile,
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description']
        )
        if commit:
            digitized_object.save()
        return digitized_object


class UserDigitizedObjectNoteForm(forms.Form):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Provide an image of the object',
            }
        )
    )
    caption = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'text-field base-input',
                'placeholder': 'Provide a caption for the image'
            }
        )
    )

    def save(self, user_digitized_object, commit=True):
        journal_entry = UserDigitizedObjectJournal(
            digit=user_digitized_object,
            image=self.cleaned_data['image'],
            caption=self.cleaned_data['caption']
        )
        if commit:
            journal_entry.save()
        return journal_entry
