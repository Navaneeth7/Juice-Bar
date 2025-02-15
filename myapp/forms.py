from django import forms
from .models import *
class categoriesForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields='__all__'