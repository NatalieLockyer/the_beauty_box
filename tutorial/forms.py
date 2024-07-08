from django import forms
from .widgets import CustomClearableFileInput
from .models import Tutorial


class DescriptionForm(forms.Form):
    description = forms.CharField(max_length=254)


class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        fields = '__all__'

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
