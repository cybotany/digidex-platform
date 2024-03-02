from django import forms

class _AbstractInventoryForm(forms.Form):
    class Meta:
        abstract = True 
        fields = '__all__'

    def clean(self):
        pass

    def common_method(self):
        pass


class _AbstractInventoryModelForm(forms.ModelForm):
    class Meta:
        abstract = True 
        model = None
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text-field base-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'text-field textarea'
            }),
        }

    def clean(self):
       pass

    def common_method(self):
        pass
