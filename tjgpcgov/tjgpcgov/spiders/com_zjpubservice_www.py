# -*- coding: utf-8 -*-
import scrapy


class ComZjpubserviceWwwSpider(scrapy.Spider):
    name = "com.zjpubservice.www"
    allowed_domains = ["www.zjpubservice.com"]
    start_urls = ['http://www.zjpubservice.com/']
    # 浙江省公共资源交易服务平台
    def parse(self, response):
        pass
