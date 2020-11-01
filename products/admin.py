from django.contrib import admin
from .models import Product, Category, Pattern, Decoration

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
class PatternAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'href',
    )
class DecorationAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'href',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Decoration, DecorationAdmin)