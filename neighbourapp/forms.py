from .models import Profile,Business,NeighbourHood,Post
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

class NewNeighbourHoodForm(forms.ModelForm):
    class Meta:
        model =NeighbourHood
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }