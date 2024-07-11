from django import forms

from .models import CollaborationRequest

class CollaborationForm(forms.ModelForm):
    class Meta:
        model = CollaborationRequest
        fields = ['name', 'email', 'message']