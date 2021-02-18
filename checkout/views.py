from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IMBvvFUqLuckO4oGMI7UfYFQMJC2S7BS1hOwKH4g7Fj8RRltw9MM574x2yuv4ZInxXb37U33G9OSGtB7meccld300wfW7Q386',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
