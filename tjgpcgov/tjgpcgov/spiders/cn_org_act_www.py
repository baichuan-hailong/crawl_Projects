# -*- coding: utf-8 -*-
import scrapy


class CnOrgActWwwSpider(scrapy.Spider):
    name = "cn.org.act.www"
    allowed_domains = ["www.act.org.cn"]
    start_urls = ['http://www.act.org.cn/']
    # 安徽省建筑工程招标投标监管网

    # 招标公告
    # 中标公示
    def parse(self, response):
        pass
