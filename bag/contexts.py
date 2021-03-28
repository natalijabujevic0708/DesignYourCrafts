from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product,Pattern
# from .models import Design


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    patterns = Pattern.objects.all()

    for item_id, details in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        

        total += details[0] * product.price
        product_count += details[0]
        bag_items.append({
            'item_id': item_id,
            'quantity': details[0],
            'product': product,
            'image_design': product.image.url,
            'design_id': details[1]
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'patterns' : patterns,
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
