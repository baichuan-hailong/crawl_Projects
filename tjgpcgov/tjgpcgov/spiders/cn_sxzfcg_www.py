# -*- coding: utf-8 -*-
# Author --- 百川 ---
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from tjgpcgov.items import tigpcItem
from tjgpcgov.items import BiddenItem


class CnSxzfcgWwwSpider(scrapy.Spider):
    name = "cn.sxzfcg.www"
    # allowed_domains = ["http://www.sxzfcg.cn"]
    start_urls = ['http://www.sxzfcg.cn/view.php?nav=61','http://www.sxzfcg.cn/view.php?nav=62','http://www.sxzfcg.cn/view.php?nav=63','http://www.sxzfcg.cn/view.php?nav=64','http://www.sxzfcg.cn/view.php?nav=65','http://www.sxzfcg.cn/view.php?nav=66','http://www.sxzfcg.cn/view.php?nav=67','http://www.sxzfcg.cn/view.php?nav=68','http://www.sxzfcg.cn/view.php?nav=69']

    # 山西省省级政府采购中心
    # http://www.sxzfcg.cn/view.php?nav=61&page=1
    # 货物 工程 服务
    # 招标公告
    # http://www.sxzfcg.cn/view.php?nav=61

    # 补充变更公告
    # http://www.sxzfcg.cn/view.php?nav=64

    # 中标公告
    # http://www.sxzfcg.cn/view.php?nav=67


    def parse(self, response):
        # print('-----------------------------------------------')
        # print(response.url.split('=', 1)[1])
         # type
        type = '招标公告'
        if response.url.split('=', 1)[1]=='67':
            type = '中标公告'
        # print(type)

        category = response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[1]/td[3]/span[@class='zt1']/text()").extract()[0]
        category = category.split('--', 3)[3]
        # print(category)


        currentPage  = response.xpath("/html/body/table[1]/tr/td[2]/table/tr[1]/td[@class='c_pt']/table/tr[2]/td/div[@class='zt3']/div[@class='pager']/strong/font/text()").extract()[0]
        nextPage     = int(currentPage)+1
        # print(currentPage)
        # print(nextPage)
        print('Nav'+response.url.split('=', 1)[1]+'###############################Page==='+currentPage+'===Page################################')

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
            issue_at = Selector(text=tr).xpath('//td[2]/text()').extract()[0]
            issue_at = issue_at.replace('[','')
            issue_at = issue_at.replace(']','')
            city = '山西'
            # print(title)
            # print(url)
            # print(issue_at)
            yield scrapy.Request(url, callback=self.parse_item,meta={"title":title,"type":type,"url":url,"issue_at":issue_at,"city":city,"category":category},dont_filter=True)

        next_url = response.url.split('=',2)[0]+'='+response.url.split('=',2)[1]+'&page='+str(nextPage)
        next_url = 'http://www.sxzfcg.cn/view.php?nav=61&page='+str(nextPage)
        # print(next_url)
        # print('-----------------------------------------------')

        # if (int(nextPage) < int(totalPage)):
        #     yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)

    def parse_item(self, response):
        print('@_______________@')
        biddenItem             = BiddenItem()
        biddenItem['title']    = response.meta['title']
        biddenItem['type']     = response.meta['type']
        biddenItem['category'] = response.meta['category']
        biddenItem['city']     = response.meta['city']
        biddenItem['url']      = response.meta['url']
        biddenItem['issue_at']     = response.meta['issue_at']

        # /html/body/table[1]/tbody/tr/td[@id='bk']/table[@class='cbk']/tbody/tr[1]/td[@class='c_pt']/table/tbody/tr[2]/td/table/tbody/tr[@class='bk5']/td/table/tbody/tr/td/div[@id='show']/p[1]
        # print(response.url)
        # print(response.xpath("/html/body/table[1]/tr/td[@id='bk']/table[@class='cbk']/tr[1]/td[@class='c_pt']/table/tr[2]/td/table/tr[@class='bk5']/td/table/tr/td/div[@id='show']/p").extract())

        # 详情
        descriptiArr = response.xpath("/html/body/table[1]/tr/td[@id='bk']/table[@class='cbk']/tr[1]/td[@class='c_pt']/table/tr[2]/td/table/tr[@class='bk5']/td/table/tr/td/div[@id='show']/p/text()").extract()
        description  = '/n'.join(descriptiArr)
        # print(description)
        description  = description.replace('\xa0','')
        description  = description.replace('\r','')
        description  = description.replace('\n','')
        
        biddenItem['description']     = description
        
        return biddenItem
