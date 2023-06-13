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
             callback = 'parse_item', follow = False),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//button[@data-auto-id="image-grid-expand-button"]'))),
    }

    def parse_item(self, response):
        item = ProductItem()

        # Example url -> https://www.adidas.es/zapatilla-gazelle/IG4986.html
        # Getting id spliting the url until we get IG4986
        item_url = response.request.url
        item_id = item_url.split('/')[-1].split('.')[0]
        original_price = response.xpath('//div[@class="product-price___2Mip5 gl-vspace"]/div[1]/div[1]/div[1]/div[1]').extract()
        unique_color = response.xpath('//div[@data-auto-id="color-label"]').extract()

        item['id'] = item_id
        item['title'] = response.xpath('//div[@class="product-description___1TLpA"]/h1[@data-auto-id="product-title"]').extract()
        item['brand'] = response.xpath('//div[@data-auto-id="product-category"]').extract()
        item['description'] = response.xpath('//meta[@id="meta-og-description"]/@content').extract()
        item['original_price'] = original_price
        item['availability'] = response.xpath('//div[@data-auto-id="size-selector"]/button[@class="gl-label size___2lbev"]').extract()
        item['images_urls'] = response.xpath('//picture/img/@src').extract()
        item['sizes'] = response.xpath('//div[@data-auto-id="size-selector"]/button/span/text()').extract()
        item['category_path'] = "".join(response.xpath('//div[1]/div[2]/ol/li[@typeof="ListItem"]')).extract()

        # We need to check if there's a descount
        item['current_price'] = response.xpath('//div[@class="product-price___2Mip5 gl-vspace"]/div[1]/div[1]/div[1]/div[2]').extract() or original_price
        # We need to check if there's more colors
        item['colors'] = response.xpath('//div[@class="color-chooser-grid___1ZBx_"]/a/img/@alt').extract() or unique_color
        