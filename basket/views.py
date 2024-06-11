from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity to the specific product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(request, f'Updated shade {shades} {product.name} quantity to {basket[item_id]['items_by_shades'][shades]}')
            else:
                basket[item_id]['items_by_shades'][shades] = quantity
                messages.success(request, f'Added shade {shades} {product.name} to your basket')
        else:
            basket[item_id] = {'items_by_shades' : {shades: quantity}}
            messages.success(request, f'Added shade {shades} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated "{product.name}" quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'This item "{product.name}" has been added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Add the quantity of the specific product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shades = None
    if 'product_shades' in request.POST:
        shades = request.POST['product_shades']
    basket = request.session.get('basket', {})

    if shades:
        if quantity > 0:
            basket[item_id]['items_by_shades'][shades] = quantity
            messages.success(request, f'Updated shade {shades} {product.name} quantity to {basket[item_id]['items_by_shades'][shades]}')
        else:
            del basket[item_id]['items_by_shades'][shades]
            if not basket[item_id]['items_by_shades']:
                basket.pop(item_id)
                messages.success(request, f'Removed shade {shades} {product.name} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated "{product.name}" quantity to {basket[item_id]}')
        else:
            basket.pop(items_id)
            messages.success(request, f'This item "{product.name}" has been removed from your basket')        

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove item/s from the shopping bag. """

    try:
        product = get_object_or_404(Product, pk=item_id)
        shades = None
        if 'product_shades' in request.POST:
            shades = request.POST['product_shades']
        basket = request.session.get('basket', {})

        if shades:
            del basket[item_id]['items_by_shades'][shades]
            if not basket[item_id]['items_by_shades']:
                basket.pop(item_id)
                messages.success(request, f'Removed shade {shades} {product.name} from your basket')
        else:
            basket.pop(item_id)      
            messages.success(request, f'This item "{product.name}" has been removed from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing this item: {e}')
        return HttpResponse(status=500)