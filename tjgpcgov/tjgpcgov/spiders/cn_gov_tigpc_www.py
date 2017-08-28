# -*- coding: utf-8 -*-
# Author --- 百川
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import tigpcItem
import re

class CnGovTigpcWwwSpider(scrapy.Spider):
    name = "cn_gov_tigpc_www"
    # allowed_domains = ["http://www.tigpc.gov.cn"]

    # 项目信息
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W001

    # 项目信息---->结果公告
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page=1&pagesize=10
    # 项目信息---->更正公告
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_004
    # 项目信息---->采购信息
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W001_001
    # 项目信息---->需求公示
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W005_001

    start_urls = ['http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page=1&pagesize=10']

    def parse(self, response):
        # print('################################')
        # print(response.url)
        next_page  = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='pager']/span/font/text()").extract()[0]
        print('################################page==='+next_page+'===Page################################')
        next_page  = str(int(next_page)+1)
        total_page = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='pager']/span/font/text()").extract()[1]
        next_url = 'http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page='+next_page+'&pagesize=10'
        # print(total_page)
        # print(next_url)
        for tr in response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='cur']/table/tr").extract():
            title = Selector(text=tr).xpath('//td[2]/a[@class]/text()').extract()[0]
            type = Selector(text=tr).xpath('//td[2]/a[1]/text()').extract()[0]
            url = Selector(text=tr).xpath('//td[2]/a[2]/@href').extract()[0]
            # print(title)
            # print(tr)
            # print(type)
            # print(url)
            title = title.replace('成交结果公告','')
            if len(title)>3:
                temp = title[0:4]
                # print(temp)
                if (temp == '天津市'):
                    title = title.replace(temp,'')

            time = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
            time = time.replace('[','')
            time = time.replace(']','')
            # print('######'+'######'+title+'######'+type+'######'+url+'######'+time+'######')
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"time":time})

        if (int(next_page) < int(total_page)):
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
        # print('################################TotalPage==='+total_page+'===TotalPage################################')
    def parse_item(self,response):
        tigItem             = tigpcItem()
        tigItem['title']    = response.meta['title']
        tigItem['type']     = '招标公告'
        tigItem['category'] = '政府招标'
        tigItem['city']     = '天津'
        tigItem['url']      = response.meta['url']
        tigItem['time']     = response.meta['time']
        # 详情
        l_des = ''
        for p in response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='xx_right']/center/table/tr[3]/td[@class='xx']/p").extract():
            # print(Selector(text=p).xpath('//span/text()').extract())
            p_line = Selector(text=p).xpath('//span/text()').extract()
            p_des  = ''.join(p_line)
            # print(p_des)
            l_des = l_des+p_des+'/n'

        tigItem['description'] = l_des
        print('------------------------->'+'\n''类型:'+tigItem['type']+'\n''分类:'+tigItem['category']+'\n''城市:'+tigItem['city']+'\n''标题:'+tigItem['title']+'\n''链接:'+tigItem['url']+'\n''发布时间:'+tigItem['time']+'\n''详情:'+tigItem['description'])
        # print(l_des)
        # return tigItem



