# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import BiddenItem
import re


class ComHebeiebWwwSpider(scrapy.Spider):
    name = "com.hebeieb.www"
    allowed_domains = ["www.hebeieb.com"]
    start_urls = ['http://www.hebeieb.com/tenderProject/index?page=0']
    #河北省招标投标公共服务平台 
    #招标公告

    def start_requests(self):
        for page in range(2):
          yield scrapy.Request('http://www.hebeieb.com/tenderProject/index?page='+str(page), callback=self.parse_list,dont_filter=True)
        
    def parse_list(self , response):
        print('################################Page==='+re.search("\d+",response.url).group(0)+'===Page################################')
        
        for li in response.xpath("/html/body/div[@class='con_row']/div[@class='list_right f_l']/div[@class='search_list_con gg_list']/ul/li").extract():
            title = Selector(text=li).xpath('//a/text()').extract()[0]
            issue_at = Selector(text=li).xpath("//span[@class='search_list_time']/text()").extract()[0]
            url = Selector(text=li).xpath('//a/@href').extract()[0]
            url = 'http://www.hebeieb.com'+url
            category = Selector(text=li).xpath("//div[@class='search_list_biaoqian']/span[1]/text()").extract()[0]
            category = category.replace('行业：','')
            city = Selector(text=li).xpath("//div[@class='search_list_biaoqian']/span[2]/text()").extract()[0]
            city = city.replace('地区：','')
            type = '招标公告'
            # print(title)
            # print(issue_at)
            # print(url)
            # print(category)
            # print(city)
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"issue_at":issue_at,"city":city,"category":category})

    def parse_item(self,response):
        biddenItem             = BiddenItem()
        biddenItem['title']    = response.meta['title']
        biddenItem['type']     = '招标公告'
        biddenItem['category'] = response.meta['category']
        biddenItem['city']     = response.meta['city']
        biddenItem['url']      = response.meta['url']
        biddenItem['issue_at'] = response.meta['issue_at']

        # 详情
        desc = ''
        for p in response.xpath("/html/body/div[@class='con_row']/div[@class='list_right f_l']/div[@class='article_con']/table[@class='infro_table']/tr[8]/td/p[@class='MsoNormal']").extract():
            # print(p)
            # print(Selector(text=p).xpath('//text()').extract())
            # print(Selector(text=tr).xpath('//td/text()')).extract()[0]
            # pass
            p_line = Selector(text=p).xpath('//text()').extract()
            # print(p_line)
            # 详情
            p_des  = ''.join(p_line)
            # print(str(p_des))
            desc = desc+p_des
            desc = desc.replace('\t','\n')
            desc = desc.replace('\xa0','')
            # print(desc)
            biddenItem['description']     = desc

        # print('标题：'+tigItem['title'])
        # print('类型：'+tigItem['type'])
        # print('时间：'+tigItem['time'])
        # print('城市：'+tigItem['city'])
        # print('categorys：'+tigItem['category'])
        # print('链接：'+tigItem['url'])  
        # print('详情：'+tigItem['description'])
        return biddenItem
            
            
        
       







