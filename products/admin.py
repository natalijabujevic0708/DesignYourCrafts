from django.contrib import admin
from .models import Product, Category, Pattern, Decoration, Icon

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
        'category_image'
    )
class PatternAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'href',
    )
class DecorationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'decoration_image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Decoration, DecorationAdmin)
admin.site.register(Icon)