# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import tigpcItem


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



    # iframe
    def parse(self, response):
        print('@++++++++++++++++++++++++++++++++++++@')
        print(response.url)

        for li in response.xpath("/html/body/form[@id='jyform']/div[@class='clearfix']/div[@id='jytypetext']/div[@class='clearfix  isshowdisplay']/div[@class='l']/div[@class='infor-bd clearfix']/ul[@class='infor-items']/div[@id='jyform:refreshData']/div[@id='jyform:refreshData_content']/table[@class='ui-datagrid-data']/tbody//tr[@class='ui-datagrid-row']/td[@class='ui-datagrid-column']/li[@class='notice-item infor-item clearfix']").extract():
            # pass
            # print(li)
            title =  Selector(text=li).xpath("//div[@class='notice-block l']/a/text()").extract()[0]
            # \n\t\t
            title = title.replace('\n','')
            title = title.replace('\t','')

            type = '中标公告'
            city =  Selector(text=li).xpath("//span[@class='infro-span'][1]/text()").extract()[0]
            city = city.replace('【','')
            city = city.replace('】','')
            time =  Selector(text=li).xpath("//span[@class='notice-date ']/text()").extract()[0]
            url =  Selector(text=li).xpath("//div[@class='notice-block l']/a/@href").extract()[0]
            url = 'http://www.zjpubservice.com'+url
            # print(str(title))
            # print(city)
            # print(time)
            # print(url)
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"time":time,"city":city},dont_filter=True)

        print('@++++++++++++++++++++++++++++++++++++@')
        # pass

    def parse_item(self, response):
        # pass
        print('##################################')
        print(response.url)
        tigItem             = tigpcItem()
        tigItem['title']    = response.meta['title']
        tigItem['type']     = response.meta['type']
        tigItem['city']     = response.meta['city']
        tigItem['url']      = response.meta['url']
        tigItem['time']     = response.meta['time']
        

        # /html/body/div[@class='container mt10']/div[@class='row']/div[@class='article_bd']/div[@class='article_con']/table/tbody/tr[2]/td[1]/div[@class='word']/b
        des_arr = response.xpath("/html/body/div[@class='container mt10']/div[@class='row']/div[@class='article_bd']/div[@class='article_con']/table/tr/td/div[@class='word']/b/text()").extract()
        # print(des_arr)
        description = '\n'.join(des_arr)
        # print(description)
        tigItem['description']     = description
        return tigItem

        # for tr in response.xpath("/html/body/div[@class='container mt10']/div[@class='row']/div[@class='article_bd']/div[@class='article_con']/table/tr").extract():
        # 	# pass
        # 	line_arr = Selector(text=tr).xpath("//td/div[@class='word']/b/text()").extract()
        # 	# print(line_arr)
        # 	line_des  = '\n'.join(line_arr)
        # 	print(line_des)
        # 	# print(tr)





