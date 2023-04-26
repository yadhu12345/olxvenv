# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class OlxscrapPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'quotes'
        )
        self.cur = self.conn.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes(
            id int NOT NULL auto_increment, 
            property_name VARCHAR(2600),
            property_id VARCHAR(200),
            breadcrumbs VARCHAR(6000),
            price VARCHAR(200),
            image_url VARCHAR(500),
            description VARCHAR(5000),
            seller_name VARCHAR(500),
            location VARCHAR(500),
            property_type VARCHAR(500),
            bathrooms VARCHAR(20),
            bedrooms VARCHAR(20),
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):
        bread =">".join(map(str,item["breadcrumbs"]))
        pr = ' '.join(item["price"].values())
        self.cur.execute(""" insert into quotes (property_name, property_id, breadcrumbs,price,image_url,description,seller_name,location,property_type,bathrooms,bedrooms) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item["property_name"],
            item["property_id"],
            bread,
            pr,
            item["image_url"],
            item["description"],
            item["seller_name"],
            item["location"],
            item["property_type"],
            item["bathrooms"],
            item["bedrooms"],
        ))

        ## Execute insert of data into database
        self.conn.commit()
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()