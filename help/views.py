from django.shortcuts import render

# Create your views here.

def help(request):
    """ A view to return the help page """
    return render(request, 'help/help.html')