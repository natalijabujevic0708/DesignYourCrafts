import io, sys

from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib import messages

from products.models import Product
from .models import Design


def view_bag(request):
    """ A view to return the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a product to the shopping bag.
        Take a screenshot of the product and append it 
        to the product details in the bag. """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    region_value = request.POST.get('region')
    
    # Take a screenshot of the product with the defined region
    list_region_values = region_value.split(", ")
    region_value = [float(i) for i in list_region_values]
    #image_design = pyautogui.screenshot(region=tuple(region_value))

    # Convert the image to fileupload object 
    image_design_io = io.BytesIO()
    image_design.save(image_design_io, format='JPEG')
    image_design_file = InMemoryUploadedFile(image_design_io, None, product.name, 'image/jpeg',
                                  sys.getsizeof(image_design_io), None)
    

    # Save the data in to Design model
    design= Design(product=product, design_image=image_design_file)
    design.save()
    
    # Save the changes in the session
    bag = request.session.get('bag', {})
    bag[item_id] = [quantity, design.pk]
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
