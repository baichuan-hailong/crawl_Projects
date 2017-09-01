# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy


class CnCcjsptWwwSpider(scrapy.Spider):
    name = "cn.ccjspt.www"
    allowed_domains = ["www.ccjspt.cn"]
    start_urls = ['http://www.ccjspt.cn/']
    # 长春市建设工程交易服务平台

    def parse(self, response):
        pass
