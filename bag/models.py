from django.db import models
from products.models import Product


class Design(models.Model):
    """Model representing a Design. It is connected by a foreign key to
    Product. """

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    design_image = models.FileField(null=True)
    