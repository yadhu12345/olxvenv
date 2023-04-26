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
            'property_name':prod.css('span.dBLgK::text').get(),
            'property_id':prod.css('strong::text')[2].get(),
            'breadcrumbs':prod.css('a._26_tZ::text').getall(),
            'price':prod.css('span.T8y-z::text').get(),
            'image_url':prod.css('img._1Iq92::attr(src)').get(),
            'description':prod.css('p::text').get(),
            'seller_name':prod.css('div.eHFQs::text').get(),
            'location':prod.css('span._1RkZP::text').get(),
            'property_type':prod.css('span.B6X7c::text').get(),
            'bathrooms':prod.css('span.B6X7c::text')[2].get(),
            'bedrooms':prod.css('span.B6X7c::text')[1].get()
        }    