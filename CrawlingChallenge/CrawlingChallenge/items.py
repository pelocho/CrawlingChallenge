# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    current_price = scrapy.Field()
    original_price = scrapy.Field()
    availability = scrapy.Field()
    images_urls = scrapy.Field()
    id = scrapy.Field()
    colors = scrapy.Field()
    sizes = scrapy.Field()
    category_path = scrapy.Field()
