from django.db import models


class ProductTypes:
    ELECTRONICS = 'EL'
    CLOTHING = 'CL'
    FOOD = 'FD'
    choices = (
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (FOOD, 'Food')
    )


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, choices=ProductTypes.choices)
    size = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
