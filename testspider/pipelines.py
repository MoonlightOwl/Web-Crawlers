# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TestspiderPipeline(object):
    def process_item(self, item, spider):
        print("[Data Output Pipeline] Data scraped:")
        print("ID: " + str(item['id']))
        print("Name: " + item['name'])
        print("Item in stock: " + str(item['in_stock']))
        return item
