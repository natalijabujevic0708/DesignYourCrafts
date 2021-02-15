from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Pattern, Decoration, Icon, Category


# Create your views here.
def product_categories(request):
    """ A view to show product categories """
    categories = Category.objects.all()

    context = {
        'current_categories': categories,
    }

    return render(request, 'products/product_categories.html', context)


def all_products(request):
    """ A view to show products """

    products = Product.objects.all()
    query = None
    if 'category' in request.GET:
        categories = [request.GET['category']]
        products = products.filter(category__name__in=categories)
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)
    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def design_product(request, product_id):
    """ A view to show individual product that the user can personalize"""

    product = get_object_or_404(Product, pk=product_id)
    patterns = Pattern.objects.all()
    decorations = Decoration.objects.all()
    icons = Icon.objects.all()

    context = {
        'product': product,
        'patterns': patterns,
        'decorations': decorations,
        'icons': icons
    }

    return render(request, 'products/design_product.html', context)
