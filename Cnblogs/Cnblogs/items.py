# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    pass

class DocItem(scrapy.Item):
    # define the fields for your item here like:
    title        = scrapy.Field()
    detail_url   = scrapy.Field()
    descripttion = scrapy.Field()
    release_time = scrapy.Field()
    com_count    = scrapy.Field()
    red_count    = scrapy.Field()

# 标题
# 详情Url
# 描述
# 发布时间
# 评论
# 阅读量