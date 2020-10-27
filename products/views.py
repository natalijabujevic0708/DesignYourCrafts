from django.shortcuts import render, get_object_or_404
from .models import Product, Color, Pattern

# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()


    context = {
        'products': products,
     
    }

    return render(request, 'products/products.html', context)

def design_product(request, product_id):
    """ A view to show individual product that the user can personalize"""

    product = get_object_or_404(Product, pk=product_id)
    colors = Color.objects.all()
    patterns = Pattern.objects.all()

    context = {
        'product': product,
        'colors': colors,
        'patterns': patterns,
    }

    return render(request, 'products/design_product.html', context) 