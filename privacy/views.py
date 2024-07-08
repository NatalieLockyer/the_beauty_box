from django.shortcuts import render

# Create your views here.


def privacy(request):
    """ A view to return privacy policy """
    return render(request, 'privacy/privacy.html')
