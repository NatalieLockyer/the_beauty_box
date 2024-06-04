from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ A view that renders the basket content """
    return render(request, 'basket/basket.html')