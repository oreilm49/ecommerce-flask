# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
        images = scrapy.Field()
        header = scrapy.Field()
        model = scrapy.Field()
        price = scrapy.Field()
        global_category = scrapy.Field()
        category = scrapy.Field()
        brand = scrapy.Field()
        description = scrapy.Field()
        specs = scrapy.Field()
        pass