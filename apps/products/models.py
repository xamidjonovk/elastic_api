from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    ELECTRONICS = 'EL'
    CLOTHING = 'CL'
    FOOD = 'FD'
    PRODUCT_TYPES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (FOOD, 'Food'),
    ]
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, choices=PRODUCT_TYPES)
    size = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
