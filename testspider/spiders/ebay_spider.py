# -*- coding: utf-8 -*-
# EbaySpider - scrap item data from ebay.com

import json
import re
import scrapy
from scrapy.exceptions import CloseSpider

from testspider.items import TestspiderItem


class EbaySpider(scrapy.Spider):
    name = "ebaySpider"
    allowed_domains = ["ebay.com"]
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(EbaySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]

    def parse(self, response):
        try:
            item_id = re.search('/(\d+)(?:\?|$)', response.url).group(1)
        except AttributeError:
            raise CloseSpider('incorrect item page URL')

        yield scrapy.Request("http://www.ebay.com/itm/layer/" + item_id, self.parse_item)

    @staticmethod
    def parse_item(response):
        data = json.loads(response.body_as_unicode())

        item = TestspiderItem()
        item['id'] = data['summary']['itemId']
        item['name'] = data['summary']['itemTitle']
        item['in_stock'] = not data['summary']['itemEnded']
        return item
