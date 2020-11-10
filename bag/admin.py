from django.contrib import admin
from .models import Design


class DesignAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'design_image',
    )

admin.site.register(Design, DesignAdmin)