from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from checkout.models import Order

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """ Will display the User Profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
       f'This is a previous confirmation of order number {order_number}.'
       'A confirmation email was sent to you on the order date.' 
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
