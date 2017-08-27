# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TjgpcgovItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass



class tigpcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title  = scrapy.Field()
    # 招标类型
    type  = scrapy.Field()
    # 详情url
    url  = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 分类
    category  = scrapy.Field()
    # 详细内容
    description  = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # tag
    tag  = scrapy.Field()

    