from django.shortcuts import render

# Create your views here.


def error_page(request):
    """ A view to return a 404 error page """
    return render(request, 'error_page/404.html')
