import scrapy

class olx(scrapy.Spider):
    name='product'
    start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']
    def parse(self,response):
        for products in response.css('li._1DNjI'):
            yield {
                'name':products.css('span._2poNJ::text').get(),
                'price':products.css('span._2Ks63::text').get(),
                'link':products.css('a').attrib['href']
                }