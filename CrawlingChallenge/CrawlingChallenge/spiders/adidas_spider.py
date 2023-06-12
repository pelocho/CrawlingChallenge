import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from CrawlingChallenge.items import ProductItem
from scrapy.exceptions import CloseSpider

class AdidasSpider(CrawlSpider):
    name = 'adidas-spider'

    allowed_domain = ['www.adidas.es']
    start_urls = ['https://www.adidas.es/hombre?grid=true',
                 'https://www.adidas.es/mujer?grid=true',
                 'https://www.adidas.es/ninos?grid=true']
    
    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a/span[@data-auto-id="pagination-right-button"]'))),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a/div/p[@class="glass-product-card__title"]')),
             callback = 'parse_item', follow = False)
    }

    def parse_item(self, response):
        item = ProductItem()

        item['title'] = response.xpath('//div[@class="product-description___1TLpA"]/h1[@data-auto-id="product-title"]')
        item['brand'] = response.xpath('//div[@data-auto-id="product-category"]')
        
        #TODO: Investigate this fields
        #There's nothing like this field on the page of the product
        #item['description'] = response.xpath('')
        #item['id'] = response.xpath('')
        #item['availability'] = response.xpath('')

        item['current_price'] = response.xpath('//div[@class="product-price___2Mip5 gl-vspace"]')
        item['original_price'] = response.xpath()
        item['images_urls'] = response.xpath('//picture/img/@src')
        item['colors'] = response.xpath('//div[@class="color-chooser-grid___1ZBx_"]/a/img/@alt')
        item['sizes'] = response.xpath('//div[@data-auto-id="size-selector"]/button/span/text()')
        item['category_path'] = "".join(response.xpath('//div[1]/div[2]/ol/li[@typeof="ListItem"]'))
        