# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
import json
import re


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
            for page in range(6):
                yield Request('http://www.njhwzbb.com/BidNewSupervisionAPI/api/Commtent/Announcements?currentCode='+child_code+'&currentPage='+str(page)+'&operateType=all', callback=self.request_category,meta={"type":type,"child_code":child_code})


    def request_category(self, response):
        result = json.loads(response.body)
        # print(result['Data'])
        list = result['Data']
        for i in range(len(list)):
            # Title
            title = result['Data'][i]['ShortTitleName']
            # Publish Time
            issue_at = result['Data'][i]['ShowDate']
            # Detail Key
            # print(result['Data'][0]['DataKey'])
            yield Request('http://www.njhwzbb.com/BidNewSupervisionAPI/api/Commtent/AnnouncementContents?dataKey='+result['Data'][i]['DataKey']+'&currentCode='+response.meta['child_code'], callback=self.parse_item,meta={"title":title,"issue_at":issue_at,"type":response.meta['type']})


    def parse_item(self, response):
        data = {}
        data['title'] = response.meta['title']
        data['type'] = response.meta['type']
        data['issue_at'] = response.meta['issue_at']
        # city
        data['city'] = '南京'

        print('@-----------------------------------------------------------------------@')


        if response.meta['type']=='招标公告':
            result_item = json.loads(response.body)
            list = Selector(text=result_item['ContentText']).xpath('//td/text()').extract()
            # print(list)
            # tel
            telphone = list[list.index('电话：')+1]
            data['telphone'] = telphone
            # location
            location = list[list.index('项目地点：')+1]
            data['location'] = location
            # expire_at
            expire_at = list[list.index('1、投标截止时间：')+1]
            data['expire_at'] = expire_at
            # email
            email = list[list.index('邮箱：')+1]
            data['email'] = email
            # agent
            agent = list[list.index('代理机构：')+1]
            data['agent'] = agent
            # amount
            amount = list[list.index('合同估算价：')+1]
            data['amount'] = amount
            # contact
            contact = list[list.index('联系人：')+1]
            data['contact'] = contact
            # sn
            sn = list[list.index('项目批准文件编号： ')+1]
            data['sn'] = sn
            # area
            area = list[list.index('地址：')+1]
            data['area'] = area
            # condition
            condition = list[list.index('（1）资质条件：')+1]
            data['condition'] = condition

            
                      
        elif response.meta['type']=='中标公告':
            # print('222')
            result_item = json.loads(response.body)
            list = Selector(text=result_item['ContentText']).xpath('//td/text()').extract()
            # print(list)
            description = ''
            for i in range(len(list)):
                description = description+list[i]+'\n'
            # print(description)
            data['description'] = description

        elif response.meta['type']=='资审公告':
            result_item = json.loads(response.body)
            list = Selector(text=result_item['ContentText']).xpath('//td/text()').extract()
            # print(list)
            # tel
            telphone = list[list.index('电话：')+1]
            data['telphone'] = telphone
            # location
            location = list[list.index('项目地点：')+1]
            data['location'] = location
            # email
            email = list[list.index('邮箱：')+1]
            data['email'] = email
            # agent
            agent = list[list.index('代理机构：')+1]
            data['agent'] = agent
            # amount
            amount = list[list.index('合同估算价：')+1]
            data['amount'] = amount
            # contact
            contact = list[list.index('联系人：')+1]
            data['contact'] = contact
            # sn
            sn = list[list.index('项目批准文件编号： ')+1]
            data['sn'] = sn
            # area
            area = list[list.index('地址：')+1]
            data['area'] = area
            # condition
            condition = list[list.index('（1）资质条件：')+1]
            data['condition'] = condition

        print(data)









        



        


        # title = scrapy.Field()
        # type = scrapy.Field()
        # city = scrapy.Field()
        # location = scrapy.Field()
        # telphone = scrapy.Field()
        # issue_at = scrapy.Field()
        # expire_at = scrapy.Field()
        # email = scrapy.Field()
        # agent = scrapy.Field()
        # amount = scrapy.Field()
        # contact = scrapy.Field()
        # sn = scrapy.Field()
        # area = scrapy.Field()
        # condition = scrapy.Field()
        # description = scrapy.Field()


        
        # category = scrapy.Field()
        # industry = scrapy.Field()
        # demander = scrapy.Field()
        # status = scrapy.Field()
        # tag = scrapy.Field()
        # url = scrapy.Field()
        # attachment = scrapy.Field()
        
        








