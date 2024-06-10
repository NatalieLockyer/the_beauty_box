from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity to the specific product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shades = None
    if 'product_shades' in request.POST:
        shades = request.POST['product_shades']
    basket = request.session.get('basket', {})

    if shades:
        if item_id in list(basket.keys()):
            if shades in basket[item_id]['items_by_shades'].keys():
                basket[item_id]['items_by_shades'][shades] += quantity
            else:
                basket[item_id]['items_by_shades'][shades] = quantity
        else:
            basket[item_id] = {'items_by_shades' : {shades: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity 
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Add the quantity of the specific product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    shades = None
    if 'product_shades' in request.POST:
        shades = request.POST['product_shades']
    basket = request.session.get('basket', {})

    if shades:
        if quantity > 0:
            basket[item_id]['items_by_shades'][shades] = quantity
        else:
            del basket[item_id]['items_by_shades'][shades]
            if not basket[item_id]['items_by_shades']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(items_id)        

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove item/s from the shopping bag. """

    try:
        shades = None
        if 'product_shades' in request.POST:
            shades = request.POST['product_shades']
        basket = request.session.get('basket', {})

        if shades:
            del basket[item_id]['items_by_shades'][shades]
            if not basket[item_id]['items_by_shades']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)        

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)