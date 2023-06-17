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
    def process_item(self, item, spider):
        product, created_bool = Product.objects.get_or_create(id=item['id'],
                                      title=item['title'],
                                      brand=item['brand'],
                                      description=item['description'],
                                      current_price=item['current_price'],
                                      original_price=item['original_price'],
                                      category_path=item['category_path'])

        for available in item['availability']:
            availability, created_bool = Size.objects.get_or_create(size=available,
                                                                     availability=True)
            product.availability.add(availability)

        for image_data in item['images_urls']:
            image, created_bool = Image.objects.get_or_create(url=image_data)
            product.images_url.add(image)

        for color_data in item['colors']:
            color, created_bool = Color.objects.get_or_create(name=color_data)
            product.colors.add(color)
        
        for size_data in item['sizes']:
            size, created_bool = Size.objects.get_or_create(size=size_data,
                                                            availability=False)
            product.sizes.add(size)

        return item
