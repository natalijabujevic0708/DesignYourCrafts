from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.product_categories, name='product_categories'),
    path('categories/products', views.all_products, name='products'),
    path('<product_id>', views.design_product, name='design_product'),
]