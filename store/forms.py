from django import forms

from .models import (
    HeadLines
)


class HeadlineForm(forms.ModelForm):
    class Meta:
        model = HeadLines
        fields = ['headline', 'image']
        