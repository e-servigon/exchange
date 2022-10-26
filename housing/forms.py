from django import forms
from django.forms import Textarea 
from .models import *

class TranslateTextsForm(forms.ModelForm):
    class Meta:
        model = TranslateTexts
        widgets = {'text_to_translate': Textarea(attrs= {'cols': 80, 'rows': 10})}
        fields = ['text_to_translate','language_code_destiny']

class FotoForm(forms.ModelForm):
    class Meta:
        model = UploadFoto
        fields=['image_to_upload']