# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    in_stock = scrapy.Field()
