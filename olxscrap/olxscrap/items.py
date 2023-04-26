# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field
from scrapy.item import Item


class OlxscrapItem(scrapy.Item):
    
    property_name = Field()
    property_id = Field()
    breadcrumbs = Field()
    price = Field()
    image_url = Field()
    description = Field()
    seller_name = Field()
    location = Field()
    property_type = Field()
    bathrooms = Field()
    bedrooms = Field()