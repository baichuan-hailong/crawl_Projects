# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import tigpcItem

class CnGovTigpcWwwSpider(scrapy.Spider):
    name = "cn_gov_tigpc_www"
    # allowed_domains = ["www.tigpc.gov.cn","*"]
    # 项目信息---->结果公告
    start_urls = ['http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page=1&pagesize=10']
    # http://www.tjgpc.gov.cn/
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page=2&pagesize=10
    def parse(self, response):
        # print('################################')
        # print(response.url)
        next_page  = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='pager']/span/font/text()").extract()[0]
        next_page  = str(int(next_page)+1)
        total_page = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='pager']/span/font/text()").extract()[1]
        next_url = 'http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page='+next_page+'&pagesize=10'
        print('################################page==='+next_page+'===Page################################')
        # print(total_page)
        # print(next_url)
        # /html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='cur']/table/tbody/tr[1]/td[2]/a[@class='xianshiwenti project_title']
        # title      = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/td[3]/text()").extract()[0]
        # print(title)
        # print(response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='cur']/table").extract()[0])
        
        for tr in response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='cur']/table/tr").extract():
            title = Selector(text=tr).xpath('//td[2]/a[@class]/text()').extract()[0]
            type = Selector(text=tr).xpath('//td[2]/a[1]/text()').extract()[0]
            url = Selector(text=tr).xpath('//td[2]/a[1]/@href').extract()[0]
            # print(title)
            # print(tr)
            # print(type)
            # print(url)
            time = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
            # print('######'+'######'+title+'######'+type+'######'+url+'######'+time+'######')
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"time":time})
        print('################################TotalPage==='+total_page+'===TotalPage################################')

        # if (int(next_page) < int(total_page)):
            # yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
        # pass

    def parse_item(self,response):
    	# tigItem          = tigpcItem()
    	# tigItem['title'] = response.meta['title']
    	# tigItem['type']  = response.meta['type']
    	# tigItem['url']   = response.meta['url']
    	# tigItem['time']  = response.meta['time']
    	print('@________________________________________________@')
    	print(response.url)
    	
    	print(response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']").extract())
        
        # print(tigItem)
        # print('-------------------+>  '+'\n''类型:'+tigItem['type']+'\n''标题:'+tigItem['title']+'\n''链接:'+tigItem['url']+'\n''发布时间:'+tigItem['time']+'\n\n\n')
        # /html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='xx_right']/center/table/tbody/tr[3]/td[@class='xx']/p[1]/span
        # /html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='xx_right']/center/table/tbody/tr[3]/td[@class='xx']/p[1]





