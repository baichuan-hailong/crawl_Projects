# -*- coding: utf-8 -*-
import scrapy


class CnSxzfcgWwwSpider(scrapy.Spider):
    name = "cn.sxzfcg.www"
    allowed_domains = ["http://www.sxzfcg.cn"]
    start_urls = ['http://www.sxzfcg.cn/default.html']

    def parse(self, response):
        pass
