from django.db import models

class Size(models.Model):
    size = models.CharField(max_length=10)
    availability = models.BooleanField()

    def __str__(self):
        return self.size

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Image(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url

class Product(models.Model):
    #For saving lists into some fields I decided to create a many-to-many relationship
    #that way we can save some sizes (for example) in sizes table and link it to this product
    #making easy the way to retrieve all the stored data about the product
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
