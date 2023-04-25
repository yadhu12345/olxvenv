import scrapy


class olx(scrapy.Spider):
    name='product'
    start_urls=['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']
    
    def parse(self,response):
        for products in response.css('li._1DNjI'):
            next_page = products.css('a').attrib['href']
            if next_page is not None:
                yield response.follow(next_page,callback=self.details)
    def details(self,response):
        prod=response.css('main._1oFYt.qmRfv')
        yield{
            'price':prod.css('span.T8y-z::text').get(),
            'property_name':prod.css('span.dBLgK::text').get(),
            'property_id':prod.css('strong::text').get()
        }    