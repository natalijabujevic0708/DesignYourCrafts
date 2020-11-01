from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_lock =  models.ImageField(null=True, blank=True)
    svg_path = models.CharField(max_length=1000, null=True, blank=True)
    svg_id = models.CharField(max_length=254, null=True, blank=True)
    top_svg_path = models.CharField(max_length=1000, null=True, blank=True)
    top_svg_id = models.CharField(max_length=254, null=True, blank=True)
    bottom_svg_path = models.CharField(max_length=1000, null=True, blank=True)
    bottom_svg_id = models.CharField(max_length=254, null=True, blank=True)
    viewBox_width = models.CharField(max_length=254, null=True, blank=True)
    viewBox_height = models.CharField(max_length=254, null=True, blank=True)
    svg_width = models.CharField(max_length=1000, null=True, blank=True)
    svg_height = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

class Decoration(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    href = models.CharField(max_length=1000, null=True, blank=True)

class Pattern(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    href = models.CharField(max_length=1000, null=True, blank=True)
   


    