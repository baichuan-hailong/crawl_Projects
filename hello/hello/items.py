# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HelloItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class zhaobiaoItem(scrapy.Item):
	"""docstring for ClassName"""
	title=scrapy.Field()
	type=scrapy.Field()
	issue_at=scrapy.Field()
	url=scrapy.Field()
	descption=scrapy.Field()

