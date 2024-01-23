from PIL import Image
from io import BytesIO
from django import forms
from django.core.files.base import ContentFile
from digit.accounts.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'avatar',)

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)

        if self.cleaned_data['avatar']:
            avatar = self.cleaned_data['avatar']
            image = Image.open(avatar)

            # Resize/modify the image
            image = image.convert('RGB')
            image.thumbnail((800, 800), Image.ANTIALIAS)

            # Save the modified image
            temp = BytesIO()
            image.save(temp, format='JPEG')
            temp.seek(0)

            # Save image to the ImageField
            profile.avatar.save(avatar.name, ContentFile(temp.read()), save=False)

        if commit:
            profile.save()
        return profile
