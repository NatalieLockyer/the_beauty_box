from django import forms

from .models import Blog, Comment
from .widgets import CustomClearableFileInput


class DescriptionForm(forms.Form):
    description = forms.CharField(max_length=254)


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
