# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import BiddenItem


class ComZjpubserviceWwwSpider(scrapy.Spider):
    name = "com.zjpubservice.www"
    allowed_domains = ["www.zjpubservice.com"]
    start_urls = ['http://www.zjpubservice.com/zjggzy/frontpage/jiaoyiinfogov/jiaoyiinfogov.jspx']
    # 浙江省公共资源交易服务平台

    # 工程建设、政府采购的中标候选人公示
    # 资格预审公告
    # 开标结果公示
    # 中标结果公告
    # 招标公告

    # 详情
    # http://www.zjpubservice.com/ --------- 002/002001/002001001/20170829/d8a05eef-09a4-44ab-ac18-651f85978d2e.html
    def parse(self, response):
        for li in response.xpath("/html/body/form[@id='jyform']/div[@class='clearfix']/div[@id='jytypetext']/div[@class='clearfix  isshowdisplay']/div[@class='l']/div[@class='infor-bd clearfix']/ul[@class='infor-items']/div[@id='jyform:refreshData']/div[@id='jyform:refreshData_content']/table[@class='ui-datagrid-data']/tbody//tr[@class='ui-datagrid-row']/td[@class='ui-datagrid-column']/li[@class='notice-item infor-item clearfix']").extract():
            # print(li)
            title =  Selector(text=li).xpath("//div[@class='notice-block l']/a/text()").extract()[0]
            # \n\t\t
            title = title.replace('\n','')
            title = title.replace('\t','')

            type = '招标公告'
            city =  Selector(text=li).xpath("//span[@class='infro-span'][1]/text()").extract()[0]
            city = city.replace('【','')
            city = city.replace('】','')
            issue_at =  Selector(text=li).xpath("//span[@class='notice-date ']/text()").extract()[0]
            url =  Selector(text=li).xpath("//div[@class='notice-block l']/a/@href").extract()[0]
            url = 'http://www.zjpubservice.com'+url
            # print(str(title))
            # print(city)
            # print(issue_at)
            print(url)
            # yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"issue_at":issue_at,"city":city},dont_filter=True)


    def parse_item(self, response):
        # pass
        print('##################################')
        biddenItem             = BiddenItem()
        biddenItem['title']    = response.meta['title']
        biddenItem['type']     = response.meta['type']
        biddenItem['city']     = response.meta['city']
        biddenItem['url']      = response.meta['url']
        biddenItem['issue_at'] = response.meta['issue_at']
        
        #详情 
        des_arr = response.xpath("/html/body/div[@class='container mt10']/div[@class='row']/div[@class='article_bd']/div[@class='article_con']/table/tr/td/div[@class='word']/b/text()").extract()
        # print(des_arr)
        description = '\n'.join(des_arr)
        # print(description)
        biddenItem['description'] = description
        return biddenItem

    





