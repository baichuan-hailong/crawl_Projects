# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SeScrwalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BlogDocItem(scrapy.Item):
	title        =scrapy.Field()
	jumpHeaderUrl=scrapy.Field()
	descption    =scrapy.Field()
	release_time =scrapy.Field()
	comment_count =scrapy.Field()
	reading_count=scrapy.Field()
	