# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy


class CnGovCcgpLiaoningWwwSpider(scrapy.Spider):

	# 辽宁政府采购网

    name = "cn.gov.ccgp-liaoning.www"
    allowed_domains = ["www.ccgp-liaoning.gov.cn"]
    start_urls = ['http://www.ccgp-liaoning.gov.cn/']
    
    def parse(self, response):
    	print("*************************************************************************")
    	# pass
