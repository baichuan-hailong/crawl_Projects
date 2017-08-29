# -*- coding: utf-8 -*-
import scrapy


class CnGovCcgpLiaoningWwwSpider(scrapy.Spider):
    name = "cn.gov.ccgp-liaoning.www"
    allowed_domains = ["www.ccgp-liaoning.gov.cn"]
    start_urls = ['http://www.ccgp-liaoning.gov.cn/']
    # 辽宁政府采购网

    # 省级和市级下的采购公告
    # 单一来源
    # 采购文件
    # 变更公告
    # 结果公告

    def parse(self, response):
        pass
