from django.shortcuts import render

# Create your views here.

def blogs(request):
    """ A view to return the beauty blog page """
    return render(request, 'blogs/blogs.html')