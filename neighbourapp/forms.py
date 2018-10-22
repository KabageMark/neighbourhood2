from .models import Profile,Business
from django import forms
#......
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }