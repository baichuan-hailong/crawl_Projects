# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hello.items import zhaobiaoItem
from scrapy.http import Request
from scrapy.selector import Selector
import re


class CnGovCcgpBeijingWwwSpider(CrawlSpider):
    name = 'cn_gov_ccgp-beijing_www'
    allowed_domains = ['www.ccgp-beijing.gov.cn']
    start_urls = ['http://www.ccgp-beijing.gov.cn/']

    def start_requests(self):
        yield Request('http://www.ccgp-beijing.gov.cn/xxgg/index.html', callback=self.parse_cate)

    def parse_cate(self, response):
        for li in response.xpath('/html/body/div[1]/div[1]/div/div/div[1]/div[1]/ul/li/@id').extract():
            print(li)
            yield Request('http://www.ccgp-beijing.gov.cn/xxgg/'+li,callback=self.parse_list)
        # i = zhaobiaoItem()
        # i['title'] = response.xpath('/html/body/ul/li[1]/a/text()')
        # i['url'] = response.xpath('/html/body/ul/li[1]/a/@href')

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # print(i)
        # return i

    def parse_list(self,response):
        for li in response.xpath('/html/body/ul/li').extract():
            data = {}
            data['url'] = Selector(text=li).xpath('//a/@href').extract()[0]
            data['title'] = Selector(text=li).xpath('//a/text()').extract()[0]
            yield Request(re.sub(r'\w+\.html$','',response.url)+data['url'].replace('./',''), callback=self.parse_item,meta={"data":data},dont_filter=True)
        next_page = response.xpath('/html/body/div/a[text()="下一页"]/@href').extract()
        for i in range(100):
            print()
            print(re.sub(r'index([\d_]*)\.html$','index_{}.html'.format(i),response.url))
            yield Request(re.sub(r'index([\d_]*)\.html$','index_{}.html'.format(i),response.url),callback=self.parse_item,dont_filter=True)

    def parse_item(self, response):
        i = zhaobiaoItem()
        i['title'] = response.meta['data']['title']
        i['url'] = response.meta['data']['url']
        i['descption'] = response.xpath('/html/body/div[1]/div[3]//text()').extract()
        i['descption'] = '\n'.join([des for des in i['descption']])
        i['descption'] = re.sub(r'\s+','\n',i['descption'])

        return i
