from django import forms
from .models import Movie

class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=('title','length','release_year')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'length':forms.NumberInput(attrs={'class':'form-control'}),
            'release_year':forms.NumberInput(attrs={'class':'form-control'}),

            }
