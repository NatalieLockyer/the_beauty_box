from django import forms
from .widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from .models import Blog

class DescriptionForm(forms.Form):
    description = forms.CharField(widget=SummernoteWidget())


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget()
        }

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
