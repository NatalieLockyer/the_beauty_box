from django.shortcuts import render, get_object_or_404
from .models import Tutorial

# Create your views here.

def all_tutorials(request):
    """ A view to show all tutorial videos, including sorting and search queries """
    
    tutorials = Tutorial.objects.all()
    
    