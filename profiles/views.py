from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from products.models import Product, Pattern

from checkout.models import Order
import ast, json


@login_required
def profile(request):
    """ Display the user's profile with past orders and past design """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    patterns = Pattern.objects.all()
    orders = profile.orders.all()
    design_history=[]
    product_id =[]
    if orders:
        for order in orders:
            product_id.extend(ast.literal_eval(order.original_bag).keys())
            design_list = ast.literal_eval(order.design)
            if len(design_list)>1:
                for design in design_list:
                    design_history.append(design)
            else:
                design_history.append(design_list[0])
    products=[]
    if product_id:
        for id in product_id:
            products.append(get_object_or_404(Product, pk=id))

    template = 'profiles/profile.html'
    context = {
        'products': products,
        'design_history': json.dumps(design_history),
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)