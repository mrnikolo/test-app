from django import forms
from .models import Text


class TextUpdateForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('body', )
