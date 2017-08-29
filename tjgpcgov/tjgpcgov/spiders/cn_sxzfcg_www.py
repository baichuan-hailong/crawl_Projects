# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import tigpcItem


class CnSxzfcgWwwSpider(scrapy.Spider):
    name = "cn.sxzfcg.www"
    # allowed_domains = ["http://www.sxzfcg.cn"]
    start_urls = ['http://www.sxzfcg.cn/view.php?nav=61','http://www.sxzfcg.cn/view.php?nav=64','http://www.sxzfcg.cn/view.php?nav=67']
    
    # 山西省省级政府采购中心
    # http://www.sxzfcg.cn/view.php?nav=61&page=1

    # 招标公告
    # http://www.sxzfcg.cn/view.php?nav=61

    # 补充变更公告
    # http://www.sxzfcg.cn/view.php?nav=64

    # 中标公告
    # http://www.sxzfcg.cn/view.php?nav=67


    def parse(self, response):
        print('-----------------------------------------------')
        # print(response.url)

        currentPage  = response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[2]/td/div[@class='zt3']/div[@class='pager']/strong/font/text()").extract()[0]
        nextPage     = int(currentPage)+1
        # print(currentPage)
        # print(nextPage)
        print('################################Page==='+currentPage+'===Page################################')

        totalPage    = response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[2]/td/div[@class='zt3']/div[@class='pager']/a[text()='最后一页 »']/@href").extract()[0]
        totalPage    = totalPage.split('=', 2)[2]
        # print('total---'+totalPage)

        # /html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[1]/td[@class='c_pt']/table/tbody/tr[2]/td/div[@class='zt3']/table[@id='node_list']/tbody/tr[@class='odd'][1]/td[1]/a
        # print('tr-------------------------------------->')
        for tr in response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[2]/td/div[@class='zt3']/table[@id='node_list']/tbody/tr").extract():
            # print(tr)
            title = Selector(text=tr).xpath('//td[1]/a/text()').extract()[0]
            url = Selector(text=tr).xpath('//td[1]/a/@href').extract()[0]
            url = 'http://www.sxzfcg.cn/'+url
            time = Selector(text=tr).xpath('//td[2]/text()').extract()[0]
            time = time.replace('[','')
            time = time.replace(']','')
            type = '招标公告'
            city = '山西'
            # print(title)
            # print(url)
            # print(time)
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"time":time,"city":city},dont_filter=True)

        next_url = response.url.split('=',2)[0]+'='+response.url.split('=',2)[1]+'&page='+str(nextPage)
        next_url = 'http://www.sxzfcg.cn/view.php?nav=61&page='+str(nextPage)
        # print(next_url)
        # print('-----------------------------------------------')

        # if (int(nextPage) < int(totalPage)):
        #     yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)

    def parse_item(self, response):
        print('@_______________@')
        tigItem             = tigpcItem()
        tigItem['title']    = response.meta['title']
        tigItem['type']     = response.meta['type']
        tigItem['category'] = '政府采购'
        tigItem['city']     = response.meta['city']
        tigItem['url']      = response.meta['url']
        tigItem['time']     = response.meta['time']



        # /html/body/table[1]/tbody/tr/td[@id='bk']/table[@class='cbk']/tbody/tr[1]/td[@class='c_pt']/table/tbody/tr[2]/td/table/tbody/tr[@class='bk5']/td/table/tbody/tr/td/div[@id='show']/p[1]
        print(response.url)
        # print(response.xpath("/html/body/table[1]/tr/td[@id='bk']/table[@class='cbk']/tr[1]/td[@class='c_pt']/table/tr[2]/td/table/tr[@class='bk5']/td/table/tr/td/div[@id='show']/p").extract())

        # 详情
        descriptiArr = response.xpath("/html/body/table[1]/tr/td[@id='bk']/table[@class='cbk']/tr[1]/td[@class='c_pt']/table/tr[2]/td/table/tr[@class='bk5']/td/table/tr/td/div[@id='show']/p/text()").extract()
        description  = '/n'.join(descriptiArr)
        # print(description)
        description  = description.replace('\xa0','')
        description  = description.replace('\r','')
        description  = description.replace('\n','')
        
        tigItem['description']     = description
        # for p in response.xpath("/html/body/table[1]/tr/td[@id='bk']/table[@class='cbk']/tr[1]/td[@class='c_pt']/table/tr[2]/td/table/tr[@class='bk5']/td/table/tr/td/div[@id='show']/p").extract():
            # pass
            # print(Selector(text=p).xpath('//text()').extract()[0])
            # p_line = Selector(text=p).xpath('//text()').extract()[0]
            # print(p_line)
            # description = description+p_line
            # print(description)
            # if len(p_line)>3:
            #     description = description+p_line+'/n'
            # print(description)
        # pass
        return tigItem
