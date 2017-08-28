# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import tigpcItem


class ComHebeiebWwwSpider(scrapy.Spider):
    name = "com.hebeieb.www"
    # allowed_domains = ["http://www.hebeieb.com/tenderProject/index"]
    start_urls = ['http://www.hebeieb.com/tenderProject/index?page=0']

    page = 0

    def parse(self, response):
        print('-----------------------------------------------')
        print(response.url)
        # print(response.xpath("/html/head/title/text()").extract()[0])
        # print(response.xpath("/html/body/div[@id='Pagination']").extract()[0])
        # print(response.xpath("/html/body/div[@id='Pagination']/span[@class='current']/text()").extract())
        # print('-----------------------------------------------')

        print('################################Page==='+str(self.page)+'===Page################################')


        for li in response.xpath("/html/body/div[@class='con_row']/div[@class='list_right f_l']/div[@class='search_list_con gg_list']/ul/li").extract():
            title = Selector(text=li).xpath('//a/text()').extract()[0]
            time = Selector(text=li).xpath("//span[@class='search_list_time']/text()").extract()[0]
            url = Selector(text=li).xpath('//a/@href').extract()[0]
            url = 'http://www.hebeieb.com'+url
            category = Selector(text=li).xpath("//div[@class='search_list_biaoqian']/span[1]/text()").extract()[0]
            category = category.replace('行业：','')
            city = Selector(text=li).xpath("//div[@class='search_list_biaoqian']/span[2]/text()").extract()[0]
            city = city.replace('地区：','')
            type = '招标公告'
            # print(title)
            # print(time)
            # print(url)
            # print(category)
            # print(city)
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"time":time,"city":city,"category":category})

        if self.page<900:
        	self.page = self.page+1
        	yield scrapy.Request('http://www.hebeieb.com/tenderProject/index?page='+str(self.page), callback=self.parse)
        	# pass
    def parse_item(self,response):
        tigItem             = tigpcItem()
        tigItem['title']    = response.meta['title']
        tigItem['type']     = '招标公告'
        tigItem['category'] = response.meta['category']
        tigItem['city']     = response.meta['city']
        tigItem['url']      = response.meta['url']
        tigItem['time']     = response.meta['time']

        print('#############################################################')
        # print(response.url)

        # /html/body/div[@class='con_row']/div[@class='list_right f_l']/div[@class='article_con']/table[@class='infro_table']/tbody/tr[8]/td/p[@class='MsoNormal']
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
            tigItem['description']     = desc

        print('标题：'+tigItem['title'])
        print('类型：'+tigItem['type'])
        print('时间：'+tigItem['time'])
        print('城市：'+tigItem['city'])
        print('categorys：'+tigItem['category'])
        print('链接：'+tigItem['url'])  
        print('详情：'+tigItem['description'])
        # return tigItem
            
            
        
       







