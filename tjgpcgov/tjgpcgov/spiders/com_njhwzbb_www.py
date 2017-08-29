# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class ComNjhwzbbWwwSpider(scrapy.Spider):
    name = "com.njhwzbb.www"
    allowed_domains = ["www.njhwzbb.com"]
    # start_urls = ['http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102320&time=1503998651','http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102431&time=1503998685']
    start_urls = ['http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102320']
    # 南京货物招标投标监督平台

    # 招标公告
    # http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102320&time=1503998651

    # 资审公告
    # http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102340&time=1503998669

    # 中标公告
    # http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102431&time=1503998685

    def parse(self, response):
        # pass
        print('@___________________________________@')
        print(response.url)
        type = '中标公告'
        if response.url == 'http://www.njhwzbb.com/app/index/column/indexColumnBidAnnounce.html?currentCode=4100000&parentCode=102300&childCode=102320&time=1503998651':
        	# pass
        	type = '招标公告'
        print(type)

        # /html/body/div/div[@id='BidSupervisionPage']/div[@class='bidSupervisionSection']/div[@class='bidSupervisionMain']/div[@id='conter']/div[@id='help-right']/div[@class='right-content-list-box']/div[@class='right-content-list'][1]/div[@class='right-content-left']
        # print(response.xpath("//div[@class='right-content-list-box']/div[@class='right-content-list']/div[@class='right-content-left']//text()").extract())
        # right-content-right
        title = response.xpath("/html/body/div/div[@id='BidSupervisionPage']/div[@class='bidSupervisionSection']/div[@class='bidSupervisionMain']/div[@id='conter']/div[@id='help-right']/div[@class='right-content-list-box']/div[@class='right-content-list']/div[@class='right-content-left']")
        print(title)
        print('@___________________________________@')
