from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Tutorial

class DescriptionForm(forms.Form):
    description = forms.CharField(widget=SummernoteWidget())


class TutorialForm(forms.ModelForm):
    
    class Meta:
        model = Tutorial
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget()
        }

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
