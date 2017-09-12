# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest


class ComNjhwzbbWwwSpider(scrapy.Spider):
    # 南京货物招标投标监督平台
    name            = "com.njhwzbb.www"
    allowed_domains = ["www.njhwzbb.com"]
    start_urls      = ['http://www.njhwzbb.com']


    childCode= ["102320","102340","102431"]
    category = ["招标公告","资审公告","中标公告"]


    def start_requests(self):
        print('@___________________________________Start___________________________________@')
        for index,child_code in enumerate(self.childCode):
            type = self.category[index]
            yield Request('http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode='+child_code, callback=self.request_category,meta={"type":type})


    def request_category(self, response):
        print(response.meta['type'])
        print(response.url)

        if response.meta['type']=='招标公告':
            print('111')
            print(response.xpath("/html/body/div/div[@id='BidSupervisionPage']/div[@class='bidSupervisionSection']/div[@class='bidSupervisionMain']/div[@class='mainHead']/div[@class='mainHeadTabs']/ul[@class='lt tabsUl']/li[@class='lt tabLi'][1]").extract())
            print(response.body)
        elif response.meta['type']=='中标公告':
            print('222')
            print(response.xpath("/html/body/div/div[@id='BidSupervisionPage']/div[@class='bidSupervisionSection']/div[@class='bidSupervisionMain']/div[@id='conter']/div[@id='help-right']/div[@class='right-content-list-box']/div[@class='right-content-list']").extract())

        elif response.meta['type']=='资审公告':
            print('3333')
            print(response.xpath("/html/body/div/div[@id='BidSupervisionPage']/div[@class='bidSupervisionSection']/div[@class='bidSupervisionMain']/div[@id='conter']/div[@id='help-right']/div[@class='right-content-list-box']/div[@class='right-content-list']").extract())








