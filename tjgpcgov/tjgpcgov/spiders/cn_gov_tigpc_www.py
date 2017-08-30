# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import BiddenItem
import re

class CnGovTigpcWwwSpider(scrapy.Spider):
    name = "cn_gov_tigpc_www"
    # allowed_domains = ["http://www.tigpc.gov.cn"]
    # 需求公示、采购信息、更正公告、结果公告
    # 项目信息---->需求公示
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W005_001&page=1&pagesize=10
    # 项目信息---->采购信息
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W001_001&page=1&pagesize=10
    # 项目信息---->更正公告
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_004&page=1&pagesize=10
    # 项目信息---->结果公告
    # http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page=1&pagesize=10

    start_urls = ['http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page=1&pagesize=10','http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_004&page=1&pagesize=10','http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W001_001&page=1&pagesize=10','http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W005_001&page=1&pagesize=10']

    def parse(self, response):
        print('################################')
        # print(response.url.split('=', 3)[1])
        # type
        type = '招标公告'
        if response.url.split('=', 3)[1]=='W004_001&page':
            type = '中标公告'

        next_page  = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='pager']/span/font/text()").extract()[0]
        print('################################page==='+next_page+'===Page################################')
        next_page  = str(int(next_page)+1)
        total_page = response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='pager']/span/font/text()").extract()[1]
        next_url = 'http://www.tjgpc.gov.cn/webInfo/getWebInfoListForwebInfoClass.do?fkWebInfoclassId=W004_001&page='+next_page+'&pagesize=10'
        # print(total_page)
        # print(next_url)
        for tr in response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='cur']/table/tr").extract():
            title = Selector(text=tr).xpath('//td[2]/a[@class]/text()').extract()[0]
            category = Selector(text=tr).xpath('//td[2]/a[1]/text()').extract()[0]
            category = category.replace('[','')
            category = category.replace(']','')
            url = Selector(text=tr).xpath('//td[2]/a[2]/@href').extract()[0]
            # print(title)
            # print(tr)
            # print(category)
            # print(url)
            title = title.replace('成交结果公告','')
            if len(title)>3:
                temp = title[0:4]
                # print(temp)
                if (temp == '天津市'):
                    title = title.replace(temp,'')

            issue_at = Selector(text=tr).xpath('//td[3]/text()').extract()[0]
            issue_at = issue_at.replace('[','')
            issue_at = issue_at.replace(']','')
            # print('######'+'######'+title+'######'+category+'######'+url+'######'+time+'######')
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"issue_at":issue_at,"category":category})

        if (int(next_page) < int(total_page)):
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
        # print('################################TotalPage==='+total_page+'===TotalPage################################')
    

    def parse_item(self,response):
        biddenItem             = BiddenItem()
        biddenItem['title']    = response.meta['title']
        biddenItem['type']     = response.meta['type']
        biddenItem['category'] = response.meta['category']
        biddenItem['city']     = '天津'
        biddenItem['url']      = response.meta['url']
        biddenItem['issue_at']     = response.meta['issue_at']
        # 详情
        l_des = ''
        for p in response.xpath("/html/body/div[@class='cover']/div[@class='main']/div[@class='main-advert']/div[@class='main-cont']/div[@class='list_right']/div[@class='xx_right']/center/table/tr[3]/td[@class='xx']/p").extract():
            # print(Selector(text=p).xpath('//span/text()').extract())
            p_line = Selector(text=p).xpath('//span/text()').extract()
            p_des  = ''.join(p_line)
            # print(p_des)
            l_des = l_des+p_des+'/n'

        biddenItem['description'] = l_des
        # print('------------------------->'+'\n''type----:'+biddenItem['type']+'\n''category:'+biddenItem['category']+'\n''city----:'+biddenItem['city']+'\n''title---:'+biddenItem['title']+'\n''url-----:'+biddenItem['url']+'\n''issue_at:'+biddenItem['issue_at']+'\n''description:'+biddenItem['description'])
        return tigItem



