# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from Se_Scrwal.items import BlogDocItem
from scrapy.selector import Selector
import re


class ComCnblogsWwwSpider(CrawlSpider):
    name            = "com_cnblogs_www"
    allowed_domains = ["www.cnblogs.com"]
    start_urls      = ['http://www.cnblogs.com/']


print('###################################################################')


def start_requests(self):
       Request('http://www.cnblogs.com', callback=self.parseItem)

def parseItem(self, response):
	blog = BlogDocItem()
	blog['title'] = 'blog_title'
	return blog