# -*- coding: utf-8 -*-
import scrapy


class ComNjhwzbbWwwSpider(scrapy.Spider):
    name = "com.njhwzbb.www"
    allowed_domains = ["www.njhwzbb.com"]
    start_urls = ['http://www.njhwzbb.com/']
    # 南京货物招标投标监督平台
    def parse(self, response):
        pass
