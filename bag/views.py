import io, sys
import pyautogui


from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib import messages

# from .models import Design
from products.models import Product, Pattern, Decoration, Icon, Category

def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to the shopping bag. """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    design_id = request.POST.get('design_id')
    
    # Save the changes in the session
    bag = request.session.get('bag', {})
    bag[item_id] = [quantity, design_id]
    request.session['bag'] = bag
    
    messages.success(request, f'Added {product.name} to your bag')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    bag[item_id][0] = quantity
    messages.success(request, f'Updated {product.name} quantity to {bag[item_id][0]}')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your bag')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
