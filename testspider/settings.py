# -*- coding: utf-8 -*-

# Scrapy settings for testspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'testspider'

SPIDER_MODULES = ['testspider.spiders']
NEWSPIDER_MODULE = 'testspider.spiders'

ITEM_PIPELINES = {
    'testspider.pipelines.TestspiderPipeline': 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'testspider (+http://www.yourdomain.com)'
