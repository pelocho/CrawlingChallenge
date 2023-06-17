from django.db import models

class Size(models.Model):
    size = models.CharField(max_length=10)
    availability = models.BooleanField()

class Color(models.Model):
    name = models.CharField(max_length=50)

class Image(models.Model):
    url = models.TextField()

class Product(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    description = models.TextField()
    current_price = models.CharField(max_length=10)
    original_price = models.CharField(max_length=10)
    availability = models.ManyToManyField(Size, related_name='product_availability')
    images_url = models.ManyToManyField(Image)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size, related_name='product_sizes')
    category_path = models.CharField(max_length=25)
