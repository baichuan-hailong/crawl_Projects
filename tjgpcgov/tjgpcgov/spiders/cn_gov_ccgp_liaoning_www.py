# -*- coding: utf-8 -*-
import scrapy


class CnGovCcgpLiaoningWwwSpider(scrapy.Spider):
    name = "cn.gov.ccgp-liaoning.www"
    allowed_domains = ["www.ccgp-liaoning.gov.cn"]
    start_urls = ['http://www.ccgp-liaoning.gov.cn/']
    # 辽宁政府采购网
    def parse(self, response):
        pass
