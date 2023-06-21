# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrawlingBackend.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from CrawlingAPI.models import Product, Image, Color, Size


class CrawlingchallengePipeline:
    #Everytime a product is scraped from the page we're gonna get here the object and save it into database
    def process_item(self, item, spider):
        #In here we're gonna create the object with simple atributes and save it into db
        product, _ = Product.objects.get_or_create(id=item['id'],
                                      title=item['title'],
                                      brand=item['brand'],
                                      description=item['description'],
                                      current_price=item['current_price'],
                                      original_price=item['original_price'],
                                      category_path=item['category_path'])

        self.save_fks(item, product)

        return item


    def save_fks(self, item, product):
        #Here we're gonna add to the object in the db the foreign keys needed for saving lists
        for available in item['availability']:
            availability, _ = Size.objects.get_or_create(size=available,
                                                         availability=True)
            product.availability.add(availability)

        for image_data in item['images_urls']:
            image, _ = Image.objects.get_or_create(url=image_data)
            product.images_url.add(image)

        for color_data in item['colors']:
            color, _ = Color.objects.get_or_create(name=color_data)
            product.colors.add(color)
        
        for size_data in item['sizes']:
            size, _ = Size.objects.get_or_create(size=size_data,
                                                 availability=False)
            product.sizes.add(size)
