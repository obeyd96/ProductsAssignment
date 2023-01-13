from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=244, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unique_code = models.CharField(max_length=244, unique=True)
    SIZE_CHOICES = [
        (10, '10'),
        (20, '20'),
        (30, '30')
    ]
    size = models.IntegerField(choices=SIZE_CHOICES)
    QUALITY_CHOICES = [
        ('high', 'High'),
        ('low', 'Low'),
        ('medium', 'Medium'),
    ]
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES)


class ProductColour(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    COLOUR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    colour = models.CharField(max_length=10, choices=COLOUR_CHOICES)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='product_images/', blank=True, null=True)
