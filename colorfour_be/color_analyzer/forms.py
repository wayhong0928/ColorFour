from django import forms
from .models import ColorAnalysis

class ColorAnalysisForm(forms.ModelForm):
    class Meta:
        model = ColorAnalysis
        fields = ['user_id', 'season', 'skin_color', 'hair_color', 'eye_color', 'description']
