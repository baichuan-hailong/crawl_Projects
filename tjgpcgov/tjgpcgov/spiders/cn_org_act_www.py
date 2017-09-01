# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy


class CnOrgActWwwSpider(scrapy.Spider):
    name = "cn.org.act.www"
    allowed_domains = ["www.act.org.cn"]
    start_urls = ['http://www.act.org.cn/']
    # 安徽省建筑工程招标投标监管网
    def parse(self, response):
        pass
