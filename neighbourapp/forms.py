from .models import Profile
from django import forms
#......



class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['users']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }