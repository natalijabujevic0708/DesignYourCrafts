from django.db import models


class Category(models.Model):
    """Model representing a Category. Optional Field: friendly_name """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    category_image = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Icon(models.Model):
    """Model representing an Icon """
    name = models.CharField(max_length=254)
    icon_full = models.ImageField(null=True)
    icon_top = models.ImageField(null=True)
    icon_bottom = models.ImageField(null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """Model representing a Product. It is connected by a foreign key to
    Category and Icon. Optional Fields: sku, image_lock. """

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True)
    image_lock =  models.ImageField(null=True, blank=True)
    # Vector shape drawn over the whole element
    svg_path = models.CharField(null=True, max_length=1000)
    svg_id = models.CharField(null=True, max_length=254)
    # Vector shape drawn over the top of the element
    top_svg_path = models.CharField(null=True, max_length=1000)
    top_svg_id = models.CharField(null=True, max_length=254)
    # Vector shape drawn over the bottom of the element
    bottom_svg_path = models.CharField(null=True, max_length=1000)
    bottom_svg_id = models.CharField(null=True, max_length=254) 
    # Width and height of the SVG
    svg_width = models.CharField(null=True, max_length=1000)
    svg_height = models.CharField(null=True, max_length=1000) 
    # Icon of the product
    icon = models.ForeignKey(Icon, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Decoration(models.Model):
    """Model representing a Decoration. Optional Field: sku """

    name = models.CharField(max_length=254, null=True, blank=True)
    decoration_image = models.ImageField(null=True)


class Pattern(models.Model):
    """Model representing a Pattern. Optional Field: sku """
    
    name = models.CharField(max_length=254, null=True, blank=True)
    href = models.CharField(max_length=1000, null=True)




    
