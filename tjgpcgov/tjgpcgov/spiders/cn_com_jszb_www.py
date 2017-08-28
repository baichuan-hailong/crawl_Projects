# -*- coding: utf-8 -*-
import scrapy


class CnComJszbWwwSpider(scrapy.Spider):
    name = "cn.com.jszb.www"
    allowed_domains = ["www.jszb.com.cn"]
    start_urls = ['http://www.jszb.com.cn/']
    # 江苏省建设工程招标网
    def parse(self, response):
        pass
