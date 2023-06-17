import scrapy
import json

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from CrawlingChallenge.items import ProductItem
from scrapy.exceptions import CloseSpider

class AdidasSpider(CrawlSpider):
    name = 'adidas-spider'
    # Added for testing on local with no huge amounts of data
    item_count = 0

    allowed_domains = ['www.adidas.es']
    start_urls = ['https://www.adidas.es/hombre?grid=true',
                 'https://www.adidas.es/mujer?grid=true',
                 'https://www.adidas.es/ninos?grid=true']

    
    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a/span[@data-auto-id="pagination-right-button"]'))),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@data-auto-id="glass-hockeycard-link"]')),
             callback = 'parse_item', follow = False),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//button[@data-auto-id="image-grid-expand-button"]'))),
    }


    def parse_item(self, response):
        item = ProductItem()

        # Example url -> https://www.adidas.es/zapatilla-gazelle/IG4986.html
        # Getting id spliting the url until we get IG4986
        item_url = response.request.url
        item_id = item_url.split('/')[-1].split('.')[0]

        original_price = response.xpath('//div[@class="product-price___2Mip5 gl-vspace"]/div[1]/div[1]/div[1]/div[1]/text()').get()

        # In case there are more than one color we get 'Color del articulo: [color]' so I decided to format it and just show the color
        color_list = response.xpath('//div[@class="color-chooser-grid___1ZBx_"]/a/img/@alt').getall()
        colors_list_formated = [color.replace('Color del artículo: ', '')for color in color_list]
        # Else
        unique_color = response.xpath('//div[@data-auto-id="color-label"]/text()').get()

        #Pictures sometime has duplicated and data that's not and url
        pictures = list(dict.fromkeys(response.xpath('//source[@srcset="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="]/img/@src').getall()))
        images_url = [pic for pic in pictures if pic.startswith('https://')]

        item['id'] = item_id
        item['title'] = response.xpath('//div[@class="product-description___1TLpA"]/h1[@data-auto-id="product-title"]/span/text()').get()
        item['brand'] = response.xpath('//div[@data-auto-id="product-category"]/span/text()').get()
        item['description'] = response.xpath('//meta[@id="meta-og-description"]/@content').get()
        item['original_price'] = original_price
        item['images_urls'] = images_url
        item['category_path'] = " > ".join(response.xpath('//div[1]/div[2]/ol/li[@typeof="ListItem"]/a/span/text()').getall())
        item['current_price'] = response.xpath('//div[@class="product-price___2Mip5 gl-vspace"]/div[1]/div[1]/div[1]/div[2]/text()').get() or original_price
        item['colors'] = colors_list_formated or unique_color

        sizes_url = 'https://www.adidas.es/api/products/' + item['id'] + '/availability'

        yield scrapy.Request(
            url=sizes_url,
            callback=self.parse_item_sizes,
            meta={"item": item},
        )


    def parse_item_sizes(self, response):
        item = response.meta['item']
        product_data = json.loads(response.text)

        sizes_data = (product_data['variation_list'])
        item['sizes'] = [size['size'] for size in sizes_data]
        item['availability'] = [size['size'] for size in sizes_data if size['availability_status']=='IN_STOCK']
        
        self.item_count *= 1

        if self.item_count > 20:
            raise CloseSpider('item_exceeded')
        yield item